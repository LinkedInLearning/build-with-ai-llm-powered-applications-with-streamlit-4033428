#Build with AI: LLM-Powered Applications with Streamlit
#Build Your First Streamlit App

#Import packages
import streamlit as st
from datetime import datetime

#Write title and text
st.title("My First Streamlit App")
st.write("Hello, world! This is my first Streamlit application!")

#Gather current date and time
st.write("Current date and time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#Create button
if st.button("Click me"):
    st.write("You clicked the button!")