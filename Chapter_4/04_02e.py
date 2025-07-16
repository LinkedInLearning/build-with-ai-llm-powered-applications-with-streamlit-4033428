#Build with AI: LLM-Powered Applications with Streamlit
#Integrate the RAG Pipeline into Your Streamlit App
 
#Import packages
import streamlit as st
from openai import OpenAI
import pandas as pd
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.docstore.document import Document

#Open file with API key
with open("openai_key.txt") as f:
    my_api_key = f.read().strip()

#Initialize OpenAI client with your API key
client = OpenAI(api_key=my_api_key)

#Configure page
st.set_page_config(page_title="Chat UI")

#Write title
st.title("Integrate RAG in Streamlit App")

#Cache global resources
@st.cache_resource
#Define vector store function
def load_vector_store():
    #Load California Tour Packages data
    df = pd.read_excel("Explore_California_Tour_Packages.xlsx")

    #Combine text fields into a single column for embedding
    df["combined_text"] = (
        df["Tour_Name"].fillna("") + ". " +
        df["Tour_Description"].fillna("") + " " +
        df["Tour_Summary"].fillna("") + " " +
        df["Tour_Keywords"].fillna("") + " " +
        df["Tour_Itinerary"].fillna("")
    ).str.strip()

    #Create list of combined text entries, excluding empty strings
    text_data = df["combined_text"].loc[df["combined_text"] != ""].tolist()

    #Convert text entries into document objects
    docs = [Document(page_content=txt) for txt in text_data]
    #Initialize and run character-based text splitter
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    #Generate embeddings for each text chunk
    embeddings = OpenAIEmbeddings(openai_api_key=my_api_key)
    
    #Create and return FAISS vector store
    return FAISS.from_documents(chunks, embeddings)

#Create vector store from loaded and embedded documents
vector_store = load_vector_store()

#Create text input widget
user_query = st.text_input("Ask a question about tours:")
if user_query:
    #Perform similarity search in the vector store for the top 3 most relevant documents
    docs = vector_store.similarity_search(user_query, k=3)
    #Combine retrieved text into a single context string
    context = "\n\n---\n\n".join([d.page_content for d in docs])
    #Provide a system prompt
    prompt = (
        "You are a helpful assistant. Use the following context to answer.\n\n"
        f"{context}\n\nQuestion: {user_query}"
    )

    #Send prompt to OpenAI chat completion API
    response = client.chat.completions.create(
        #Select model
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )

    #Gather assistant's response
    bot_reply = response.choices[0].message.content.strip()
    #Display reply
    st.markdown("**Answer:**")
    st.write(bot_reply)