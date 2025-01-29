from langchain_core.prompts import ChatPromptTemplate
from langchain import hub

def quiz_generator_prompt():
    '''
    Generates Prompt template for quiz generation

    Returns:
        ChatPromptTemplate -> Configured ChatPromptTemplate instance
    '''
    system_msg = '''
        You are a quiz generation assistant. Your task is to create quizzes based on the topic and difficulty level provided by the user. Follow these guidelines:
        1. Generate a quiz containing five questions.
        2. Each question should be relevant to the topic and match the difficulty level.
        3. Format the questions clearly and concisely.
        4. Respond only with the quiz questions, without any additional explanations or descriptions.
        If the query is unrelated to quiz generation, respond with:
        "I am a quiz generation assistant. Please ask me to generate a quiz by specifying a topic and difficulty level."
    '''

    user_msg = "Generate a quiz on {topic} with difficulty level {difficulty}"

    prompt_template = ChatPromptTemplate([
        ("system", system_msg),
        ("user", user_msg)
    ])

    return prompt_template

def quiz_generator_prompt_lang():
    ''' Genetate prompt from lang 
    returns :
        prompt
    '''
    prompts = hub.pull("poem/quiz")

    return prompts
