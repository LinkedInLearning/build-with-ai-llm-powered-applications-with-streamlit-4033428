#Build with AI: LLM-Powered Applications with Streamlit
#Build Chat Features: Add Input and Display Messages
 
#Import packages
import streamlit as st

#Write title
st.title("Chat Input & Display")

#Determine if chat history exists in the session state and initialize if it doesn't
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#Create text input widget for user input
user_msg = st.text_input("You:", key="user_msg_input")

#Create button to append user's message to chat history
if st.button("Send", key="send_button"):
    if user_msg:
        st.session_state.chat_history.append(f"You: {user_msg}")

#Display all messages from chat history
for msg in st.session_state.chat_history:
    st.write(msg)
