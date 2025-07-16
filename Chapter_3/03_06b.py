#Build with AI: LLM-Powered Applications with Streamlit
#Query the Vector Database to Find Relevant Information
 
#Import packages
import streamlit as st
import numpy as np
from openai import OpenAI
import faiss
import pickle


#Open file with API key
with open("openai_key.txt") as f:
    my_api_key = f.read().strip()

#Initialize OpenAI client with your API key
client = OpenAI(api_key=my_api_key)

#Write title
st.title("")

#Create text input widget


    #Check if FAISS index file exists

        #Load FAISS index from file


        #Load stored text data and tour names


        #Embed user's search query

        #Convert embedding into numpy array and reshape for FAISS


        #Search for nearest neighbors in vector store


        #Display top matching tour names with distances

        #Loop through indices and distances of the search results

            #Display tour name and distance from query
