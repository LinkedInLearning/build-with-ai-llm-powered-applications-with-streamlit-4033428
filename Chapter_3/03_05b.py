#Build with AI: LLM-Powered Applications with Streamlit
#Create a Vector Store with Chroma for Fast Retrieval
 
#Import packages
import streamlit as st
import pandas as pd
from openai import OpenAI

#Open file with API key
with open("openai_key.txt") as f:
    my_api_key = f.read().strip()

#Initialize OpenAI client with your API key
client = OpenAI(api_key=my_api_key)

#Write title
st.title("")

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
#Display spinner message for user when embeddings are generating

    #Loop through each text string in list
    for text in df["combined_text"]:
        #Call OpenAI embeddings API to generate embedding for text
        resp = client.embeddings.create(model="text-embedding-3-small", input=text)
        embeddings.append(resp.data[0].embedding)

#Convert embeddings to numpy array


#Create FAISS index and add embeddings


#Save index


#Save text data and names separately to pickle files


#Share success message
