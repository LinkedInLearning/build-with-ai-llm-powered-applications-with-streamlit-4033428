#Build with AI: LLM-Powered Applications with Streamlit
#Generate Embeddings from Text for Searchability
 
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
st.title("Generate Embeddings")

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
def get_embeddings(texts):
    embeddings = []
    #Loop through each text string in list
    for txt in texts:
        #Call OpenAI embeddings API to generate embedding for text
        resp = client.embeddings.create(model="text-embedding-3-small", input=txt)
        embeddings.append(resp.data[0].embedding)
    return embeddings

#Create button to trigger embedding generation
if st.button("Generate Embeddings"):
    #Display spinner message for user when embeddings are generating
    with st.spinner("Generating embeddings..."):
        df["embedding"] = get_embeddings(df["combined_text"].tolist())
    #Show success message once embeddings are generated
    st.success("Embeddings generated!")
    #Display preview of embedded data
    st.write(df[["Tour_Name", "embedding"]].head())