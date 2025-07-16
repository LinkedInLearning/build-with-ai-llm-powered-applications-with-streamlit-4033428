#Build with AI: LLM-Powered Applications with Streamlit
#Create a Chat UI in Streamlit for LLM Interactions
 
#Import packages
import streamlit as st

#Configure page
st.set_page_config(page_title="Chat UI")

#Write title
st.title("Build Chat UI")

#Determine if chat history exists in the session state and initialize if it doesn't
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#Define function to handle sending messages and receiving LLM responses  
def send_message():
    #Get user input and remove whitespaces
    user_msg = st.session_state.user_msg.strip()
    #Exit function if input is empty
    if not user_msg:
        return
    #Add user's message to chat history
    st.session_state.chat_history.append(("User", user_msg))
    #Add placeholder bot response that echoes user's message
    st.session_state.chat_history.append(("Bot", f"Echo: {user_msg}"))
    #Clear text input field after message is sent
    st.session_state.user_msg = ""

#Create text input field that triggers send_message when enter button is pressed
st.text_input("User:", key="user_msg", on_change=send_message, placeholder="Type a message…")

st.markdown("**Chat History**")
#Loop through chat history and display messages
for speaker, msg in st.session_state.chat_history:
    st.write(f"**{speaker}:** {msg}")


