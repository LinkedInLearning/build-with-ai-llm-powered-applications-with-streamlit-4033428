#Build with AI: LLM-Powered Applications with Streamlit
#Integrate the RAG Pipeline into Your Streamlit App
 
#Import packages
import streamlit as st


#Open file with API key


#Initialize OpenAI client with your API key

#Configure page
st.set_page_config(page_title="Chat UI")

#Write title
st.title("")

#Cache global resources

#Define vector store function

    #Load California Tour Packages data


    #Combine text fields into a single column for embedding


    #Create list of combined text entries, excluding empty strings


    #Convert text entries into document objects

    #Initialize and run character-based text splitter


    #Generate embeddings for each text chunk

    
    #Create and return FAISS vector store


#Create vector store from loaded and embedded documents


#Create text input widget

    #Perform similarity search in the vector store for the top 3 most relevant documents

    #Combine retrieved text into a single context string

    #Provide a system prompt


    #Send prompt to OpenAI chat completion API

        #Select model


    #Gather assistant's response

    #Display reply
