import prompt
from model import create_groq_llm

def generate_quiz(topic, difficulty):
    '''
    Function to generate a quiz

    Args:
        topic (str): The topic for the quiz
        difficulty (str): The difficulty level (Easy, Medium, Hard)

    Returns:
        response.content (str): The generated quiz
    '''
    prompt_template = prompt.quiz_generator_prompt_lang()
    llm = create_groq_llm()

    chain = prompt_template | llm

    response = chain.invoke({
        "topic": topic,
        "difficulty": difficulty
    })

    return response.content
