from dotenv import load_dotenv
import streamlit as st

import chain

load_dotenv()

def poem_generation_app():
    """poem generater app
    
    """
    with st.form("poem_generater"):
        topic=st.text_input("enter the topic")
        submitted=st.form_submit_button("generate")
        if(submitted):
            # topic+=" - generate 8 line poem from the above"
            response = chain.poem(topic)
            st.info(response)

poem_generation_app()