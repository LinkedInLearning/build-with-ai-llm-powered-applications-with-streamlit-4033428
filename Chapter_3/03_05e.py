#Build with AI: LLM-Powered Applications with Streamlit
#Create a Vector Store with Chroma for Fast Retrieval
 
#Import packages
import streamlit as st
import pandas as pd
from openai import OpenAI
import faiss
import numpy as np
import pickle

#Open file with API key
with open("openai_key.txt") as f:
    my_api_key = f.read().strip()

#Initialize OpenAI client with your API key
client = OpenAI(api_key=my_api_key)

#Write title
st.title("Create FAISS Vector Store")

#Load California Tour Packages data
df = pd.read_excel("Explore_California_Tour_Packages.xlsx")

#Combine text fields into a single column for embedding
df["combined_text"] = (
    df["Tour_Name"].fillna("") + ". " +
    df["Tour_Description"].fillna("") + ". " +
    df["Tour_Summary"].fillna("") + ". " +
    df["Tour_Keywords"].fillna("") + ". " +
    df["Tour_Itinerary"].fillna("") + "."
).str.strip()

#Generate embeddings for text data
embeddings = []
#Display spinner message for user when embeddings are generating
with st.spinner("Generating embeddings..."):
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

#Save index
faiss.write_index(index, "faiss_index.idx")

#Save text data and names separately to pickle files
with open("text_data.pkl", "wb") as f:
    pickle.dump(df["combined_text"].tolist(), f)

with open("names.pkl", "wb") as f:
    pickle.dump(df["Tour_Name"].tolist(), f)

#Share success message
st.success("FAISS vector store and tour data saved to disk!")