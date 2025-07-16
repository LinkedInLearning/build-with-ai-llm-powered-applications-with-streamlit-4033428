#Build with AI: LLM-Powered Applications with Streamlit
#Construct Effective RAG Prompts for Better LLM Answers
 
#Import packages
import streamlit as st

#Write title
st.title("Construct RAG Prompts")

#Provide text area for pasting context snippets
context_snippets = st.text_area(
    "Paste retrieved context snippets (one per line):",
    height=200
).splitlines()

#Create text input widget for user's question
user_question = st.text_input("Your question:")

#Create button to build RAG prompt
if st.button("Build Prompt"):
    prompt = (
        "You are an expert tour guide. Use the following information to answer the question.\n\n"
        "Context:\n" + "\n".join(f"- {line}" for line in context_snippets) +
        "\n\nQuestion: " + user_question +
        "\n\nAnswer:"
    )
    #Display constructed prompt
    st.subheader("Constructed Prompt")
    st.code(prompt)
