#Build with AI: LLM-Powered Applications with Streamlit
#Send User Prompts to an LLM and Display the Response
 
#Import packages


#Open file with API key


#Initialize OpenAI client with your API key

#Write title


#Determine if chat history exists in the session state and initialize if it doesn't


#Define function to hand sending messages and receiving LLM responses  

    #Get user input and remove whitespaces

    #Exit function if input is empty


    #Add user's message to chat history


        #Send chat history to OpenAI LLM and receive response

            #Select model

            #Provide a system prompt

        
        #Gather assistant's response



        #Handle API errors


    #Add AI assistant's reply to chat history

    #Clear text input field after message is sent


#Create text input field that triggers send_message when enter button is pressed


#Loop through chat history and display messages

