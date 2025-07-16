#Build with AI: LLM-Powered Applications with Streamlit
#Generate Embeddings from Text for Searchability
 
#Import packages
import streamlit as st
import pandas as pd


#Open file with API key


#Initialize OpenAI client with your API key


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

#Cache computations that return data
@st.cache_data
#Create function to prepare text data for embedding

    #Loop through each text string in list

        #Call OpenAI embeddings API to generate embedding for text


#Create button to trigger embedding generation

    #Display spinner message for user when embeddings are generating

    #Show success message once embeddings are generated

    #Display preview of embedded data
