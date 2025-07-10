#Build with AI: LLM-Powered Applications with Streamlit
#Save and Display Chat History in Your Application
 
#Import packages
import streamlit as st
from openai import OpenAI
import json

#Open file with API key
with open("openai_key.txt") as f:
    my_api_key = f.read().strip()

#Initialize OpenAI client with your API key
client = OpenAI(api_key=my_api_key)

#Write title
st.title("Save and Display Chat History")

#Determine if chat history exists in the session state and initialize if it doesn't
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#Define function to hand sending messages and receiving LLM responses  
def send_message():
    #Get user input and remove whitespaces
    user_msg = st.session_state.user_msg.strip()
    #Exit function if input is empty
    if user_msg == "":
        return

    #Add user's message to chat history
    st.session_state.chat_history.append({"sender": "user", "message": user_msg})

    try:
        #Send chat history to OpenAI LLM and receive response
        response = client.chat.completions.create(
            #Select model
            model="gpt-3.5-turbo",
            #Provide a system prompt
            messages=[
                {"role": "system", "content": "You are a helpful assistant."}
            ] + [
                #Add previous messages from chat history
                {"role": "user" if m["sender"] == "user" else "assistant", "content": m["message"]}
                for m in st.session_state.chat_history
            ]
        )
        #Gather assistant's response
        bot_reply = response.choices[0].message.content.strip()

    except Exception as e:
        #Handle API errors
        bot_reply = f"[Error calling OpenAI]: {e}"

    #Add AI assistant's reply to chat history
    st.session_state.chat_history.append({"sender": "assistant", "message": bot_reply})
    #Clear text input field after message is sent
    st.session_state.user_msg = ""

#Create text input field that triggers send_message when enter button is pressed
st.text_input("You:", key="user_msg", on_change=send_message)

#Loop through chat history and display messages
for msg in st.session_state.chat_history:
    sender = "You" if msg["sender"] == "user" else "Bot"
    st.write(f"**{sender}:** {msg['message']}")

#Add button to clear chat history and refresh
if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.rerun()

#If chat history exists, convert chat history to JSON string and allow user to download as JSON file
if st.session_state.chat_history:
    json_str = json.dumps(st.session_state.chat_history, indent=2)
    st.download_button("Download Chat History", data=json_str, file_name="chat_history.json")