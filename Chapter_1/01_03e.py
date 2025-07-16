#Build with AI: LLM-Powered Applications with Streamlit
#Basic Streamlit Commands for Web Development

#Import packages
import streamlit as st

#Write header and subheader
st.header("Basic Streamlit Commands")
st.subheader("Widgets")

#Create number slider widget
number = st.slider("Pick a number", 0, 100, 25)
st.write("You picked:", number)

#Create text input widget
text = st.text_input("Enter some text")
st.write("You typed:", text)

#Create multiselect widget
options = st.multiselect("Choose pizza toppings", ["Cheese", "Pepperoni", "Onions"])
st.write("Toppings:", options)