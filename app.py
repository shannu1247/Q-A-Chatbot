import streamlit as st
import groq
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()


##LangSmith Tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT']='Simple Q&A Chatbot With GROQ'


prompt= f"""
You are an expert Python tutor.

Task:
Explain the following concept.

Concept:
"""

def generate_response(concept,api_key,llm,temperature,max_tokens):
    llm = ChatGroq(
    model=llm,
    groq_api_key=api_key)
    output_parser=StrOutputParser()
    chain=llm|output_parser
    answer=chain.invoke(prompt+concept)
    return answer
    
### Title of the app
st.title("Enhanced Q&A Chatbot With Groq") 

##sidebar for settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter Your API_KEY:",type="password")

##drop down to select various groq models
llm=st.sidebar.selectbox("Select an GROQ Model",["openai/gpt-oss-120b","qwen/qwen3-32b","openai/gpt-oss-20b"])

##Adjust resopnse parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("max_tokens",min_value=50,max_value=300,value=150)
st.write("Go ahead and ask me a question")
user_input=st.text_input("you:")

if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("please provide me the question")    



