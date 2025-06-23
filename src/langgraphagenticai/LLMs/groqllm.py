"""
Fundamental purpose of this file is: Reading the GROQ API KEY that we are 
providing in the front-end and load.
"""
import os 
import streamlit as st 
from langchain_groq import ChatGroq 


class GroqLLM:
    # Whenever we initialize this class, the first thing we need to
    # do is initialize our user controls
    def __init__(self, user_controls_input):
        # user_controls_input comes from front-end 
        self.user_controls_input = user_controls_input

    def get_llm_model(self): # specifically for loading the LLM
        try:
            groq_api_key = self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model = self.user_controls_input["selected_groq_model"]
            if groq_api_key=='' and os.environ["GROQ_API_KEY"]=='':
                st.error("Please Enter the Groq API Key.")
            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error occured with Exception : {e}")
        
        return llm 


