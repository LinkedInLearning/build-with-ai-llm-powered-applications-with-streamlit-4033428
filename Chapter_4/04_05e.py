#Build with AI: LLM-Powered Applications with Streamlit
#Test Your Chatbot to Ensure It Works Smoothly
 
#Import packages
import pytest
from rag_chatbot import load_vector_store, client

#Call on fixture function
@pytest.fixture(scope="module")
#Create vector store function
def vs():
    #Return vector store
    return load_vector_store()

#Create similarity search function
def test_similarity_search(vs):
    #Perform similarity search using dummy query
    docs = vs.similarity_search("test query", k=1)
    #Ensure one document is returned
    assert len(docs) == 1
    #Assert returned document is not empty
    assert docs[0].page_content

#Create mock OpenAI Call function
def test_openai_call(monkeypatch):
    #Simulate OpenAI choice object with a message attribute
    class DummyChoice:
        message = type("M", (), {"content":"dummy reply"})
    #Simulate OpenAI response containing a list of choices
    class DummyResp:
        choices = [DummyChoice()]
    #Create function to fake 'create' method to replace the real OpenAI call during testing
    def fake_create(**kwargs):
        return DummyResp()
    #Use monkeypatch to override OpenAI API call with the fake one
    monkeypatch.setattr(client.chat.completions, "create", fake_create)
    #Call the patched OpenAI API method
    resp = client.chat.completions.create(model="gpt-3.5-turbo", messages=[])
    #Assert the fake response content matches the expected dummy reply
    assert resp.choices[0].message.content == "dummy reply"
