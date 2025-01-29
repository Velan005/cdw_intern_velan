from dotenv import load_dotenv
import streamlit as st
import chain
 
load_dotenv()

def quiz_generator_app():
    '''
    Function to generate quiz generator app

    Returns:
        response(str)
    '''
    st.title("Quiz Generator")

    with st.form("quiz_generator"):
        topic = st.text_input("Enter the topic for the quiz")
        difficulty = st.selectbox("Select difficulty level", ["Easy", "Medium", "Hard","Master"])
        submitted = st.form_submit_button("Generate Quiz")
        
        if submitted:
            response = chain.generate_quiz(topic, difficulty)
            st.subheader("Generated Quiz")
            st.info(response)

quiz_generator_app()
