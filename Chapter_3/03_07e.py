#Build with AI: LLM-Powered Applications with Streamlit
#Implement the RAG Query Function to Combine Search + Chat
 
#Import packages type in code
import streamlit as st
import pandas as pd
import faiss
import numpy as np
from openai import OpenAI


#Open file with API key
with open("openai_key.txt") as f:
    my_api_key = f.read().strip()

#Initialize OpenAI client with your API key
client = OpenAI(api_key=my_api_key)

#Write title
st.title("RAG Query with FAISS")

#Create text input widget
user_query = st.text_input("Enter your question:")

if user_query:
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

    #Generate embeddings for text data
    embeddings = []
    #Loop through each text string in list
    for text in df["combined_text"]:
        #Call OpenAI embeddings API to generate embedding for text
        resp = client.embeddings.create(model="text-embedding-3-small", input=text)
        embeddings.append(resp.data[0].embedding)

    #Convert embeddings to numpy array
    emb_array = np.array(embeddings).astype("float32")
    #Create FAISS index and add embeddings
    index = faiss.IndexFlatL2(emb_array.shape[1])
    index.add(emb_array)

    #Embed user's question into numpy array
    query_emb = np.array(
        [client.embeddings.create(model="text-embedding-3-small", input=user_query).data[0].embedding]
    ).astype("float32")

    #Search for the 5 nearest neighbors
    D, I = index.search(query_emb, 5)

    #Retrieve top matching text snippets
    context_snippets = [df.iloc[i]["combined_text"] for i in I[0]]

    #Define system prompt
    system_prompt = "You are an expert tour guide. Use the provided information to answer user questions helpfully and concisely."

    #Construct final RAG prompt
    prompt = (
        system_prompt + "\n\n"
        "Context:\n" + "\n".join(f"- {line}" for line in context_snippets) +
        "\n\nQuestion: " + user_query +
        "\n\nAnswer:"
    )

    #Send prompt to OpenAI chat completion API
    response = client.chat.completions.create(
        #Select model
        model="gpt-3.5-turbo",
        #Provide a system prompt
        messages=[{"role": "system", "content": system_prompt},
                  {"role": "user", "content": prompt}]
    )

    ##Gather assistant's response
    st.subheader("Answer")
    st.write(response.choices[0].message.content.strip())

    #Display the text snippets used
    st.subheader("Debug Info")
    st.write("Snippets used:")
    for line in context_snippets:
        st.write("-", line)