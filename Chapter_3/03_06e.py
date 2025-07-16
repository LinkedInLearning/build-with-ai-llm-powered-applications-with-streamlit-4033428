#Build with AI: LLM-Powered Applications with Streamlit
#Query the Vector Database to Find Relevant Information
 
#Import packages
import streamlit as st
import numpy as np
from openai import OpenAI
import faiss
import pickle
import os

#Open file with API key
with open("openai_key.txt") as f:
    my_api_key = f.read().strip()

#Initialize OpenAI client with your API key
client = OpenAI(api_key=my_api_key)

#Write title
st.title("Query FAISS Vector Store")

#Create text input widget
user_query = st.text_input("Enter your search query")

if user_query:
    #Check if FAISS index file exists
    if not os.path.exists("faiss_index.idx"):
        st.error("Please run Lesson 03_05 first to create and save your vector store.")
    else:
        #Load FAISS index from file
        index = faiss.read_index("faiss_index.idx")

        #Load stored text data and tour names
        with open("text_data.pkl", "rb") as f:
            text_data = pickle.load(f)
        with open("names.pkl", "rb") as f:
            names = pickle.load(f)

        #Embed user's search query
        resp = client.embeddings.create(model="text-embedding-3-small", input=user_query)
        #Convert embedding into numpy array and reshape for FAISS
        query_emb = np.array([resp.data[0].embedding]).astype("float32")

        #Search for 3 nearest neighbors in vector store
        D, I = index.search(query_emb, 3)

        #Display top matching tour names with distances
        st.subheader("Top Relevant Tours")
        #Loop through indices and distances of the search results
        for idx, dist in zip(I[0], D[0]):
            #Display tour name and distance from query
            st.write(f"- {names[idx]} (distance: {dist:.3f})")