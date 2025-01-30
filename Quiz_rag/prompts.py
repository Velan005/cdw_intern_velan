

from langchain_core.prompts import ChatPromptTemplate
from langchain import hub

def quiz_generator_prompt():
    """
    Generates a prompt template for quiz generation with structured and visually appealing formatting.

    Returns:
        ChatPromptTemplate - Configured template with unique quiz formatting.
    """
    system_msg = """
                🎯 Welcome to the Ultimate Quiz Generator! 🎯
                
                You are an intelligent quiz creator, skilled at generating engaging multiple-choice quizzes on any topic.
                
                🔹 *Instructions for Quiz Format:* 
                1️⃣ Each question should be numbered and formatted uniquely.  
                2️⃣ Each question should have exactly 4 options labeled as *(A), (B), (C), (D)*.  
                3️⃣ Ensure proper spacing, symbols, and formatting for readability.  
                4️⃣ At the end of each question, highlight the correct answer in the format:  
                   ✅ *Correct Answer:* *Option [X] - (Answer)*  
                5️⃣ Use creative separators (🔸, 🔹, ➖, etc.) to make the quiz visually appealing.  
                
                🎭 *Example Output:*  
                ➖➖➖➖➖➖➖➖➖➖➖  
                *Q1️⃣: What is the capital of France?*  
                🔹 (A) Berlin  
                🔹 (B) Madrid  
                🔹 (C) Paris  
                🔹 (D) Rome  
                ✅ *Correct Answer:* *Option C - Paris*  
                ➖➖➖➖➖➖➖➖➖➖➖  
                
                🎯 Let's start generating quizzes in this *unique and attractive format*!  
                """

    user_msg = "Generate a unique and visually appealing quiz on the topic: {topic}"

    return ChatPromptTemplate([
        ("system", system_msg),
        ("user", user_msg)
    ])


def quiz_generator_rag_prompt():
    """
    Generates a RAG-enabled quiz prompt with structured and visually appealing formatting.

    Returns:
        ChatPromptTemplate - Configured template with context support and unique quiz formatting.
    """
    system_msg = """
                🎯 Welcome to the Ultimate Quiz Generator! 🎯
                
                You are an intelligent quiz creator with access to *external documents* for enhanced quiz generation.
                
                🔹 *Instructions for Quiz Format:*  
                1️⃣ Each question should be numbered and formatted uniquely.  
                2️⃣ Each question should have exactly 4 options labeled as *(A), (B), (C), (D)*.  
                3️⃣ Ensure proper spacing, symbols, and formatting for readability.  
                4️⃣ At the end of each question, highlight the correct answer in the format:  
                   ✅ *Correct Answer:* *Option [X] - (Answer)*  
                5️⃣ Use creative separators (🔸, 🔹, ➖, etc.) to make the quiz visually appealing.  

                📜 *Use the provided context* to generate quiz questions based on:  
                {context}

                🎯 Let's create an engaging quiz with this structured format!
                """

    user_msg = """
                Generate a unique and visually appealing quiz on the topic: {topic}
                Use the following context for generating questions:
                {context}
                """

    return ChatPromptTemplate([
        ("system", system_msg),
        ("user", user_msg)
    ])


def quiz_generator_prompt_from_hub(template="ishwaryaa/quiz_rag"):
    """
    Pulls a quiz generation prompt template from the hub.
    
    Args:
        template (str): The name of the template to be pulled from the hub.

    Returns:
        The prompt template from the hub.
    """
    prompt_template = hub.pull(template)
    return prompt_template