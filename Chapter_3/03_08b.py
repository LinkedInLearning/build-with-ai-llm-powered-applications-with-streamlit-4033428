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
st.title("")

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

    #Create FAISS index and add embeddings


    #Embed user's question into numpy array


    #Search for the 3 nearest neighbors
    D, I = index.search(query_emb, 3)

    #Retrieve top matching text snippets


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

        #Select model

        #Provide a system prompt

    ##Gather assistant's response

    #Display the text snippets used
