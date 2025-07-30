#Build with AI: LLM-Powered Applications with Streamlit
#Prepare Text Data for Embedding
 
#Import packages
import streamlit as st
import pandas as pd

#Write title
st.title("Prepare Text Data for Embedding")

#Load California Tour Packages data
df = pd.read_excel("Explore_California_Tour_Packages.xlsx")

#Display preview of raw data
st.subheader("Raw Data Preview")
st.dataframe(df.head())

#Cache computations that return data
@st.cache_data
#Create function to prepare text data for embedding
def prepare_text(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    #Replace null values with empty strings for relevant text columns
    for col in ["Tour_Description", "Tour_Summary", "Tour_Keywords", "Tour_Itinerary"]:
        df[col] = df[col].fillna("")

    #Combine text fields into a single column for embedding
    df["combined_text"] = (
        df["Tour_Name"] + ". " +
        df["Tour_Description"] + ". " +
        df["Tour_Summary"] + ". " +
        df["Tour_Keywords"] + ". " +
        df["Tour_Itinerary"] + "."
    ).str.strip()
    
    return df

#Prepare text data using function
df_prepared = prepare_text(df)

#Display prepared text data
st.subheader("Prepared Text Data")
st.dataframe(df_prepared[["Tour_Name", "combined_text"]].head())
