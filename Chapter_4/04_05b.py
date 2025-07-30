#Build with AI: LLM-Powered Applications with Streamlit
#Test Your Chatbot to Ensure It Works Smoothly
 
#Import packages


#Call on fixture function

#Create vector store function

    #Return vector store


#Create similarity search function

    #Perform similarity search using dummy query

    #Ensure one document is returned

    #Assert returned document is not empty


#Create mock OpenAI Call function

    #Simulate OpenAI choice object with a message attribute

    #Simulate OpenAI response containing a list of choices

    #Create function to fake 'create' method to replace the real OpenAI call during testing

    #Use monkeypatch to override OpenAI API call with the fake one

    #Call the patched OpenAI API method

    #Assert the fake response content matches the expected dummy reply
