# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:17:34 2025

@author: ts235
"""
import random
import streamlit as st

# Sample dataset with questions and corresponding answers
knowledge_base = [
    ["What is the capital of France?", "The capital of France is Paris."],
    ["How do you make a cake?", "To make a cake, you need to follow a recipe and bake it in an oven."],
    ["What is the largest continent in the world?", "Asia is the largest continent."],
    # Add more questions and answers as needed
]

def chatbot(user_question):
    for question, answer in knowledge_base:
        if question.lower() == user_question.lower():
            return answer

    # If the question is not found in the knowledge base, provide a random response
    random_answer = random.choice([
        "That's an interesting question! I'll need to think about it.",
        "Hmm, I'm not sure, but I can find out for you.",
        "Sorry, I don't have that information. Can you ask something else?",
    ])
    return random_answer

# Streamlit app
st.title("Simple Question Answering Chatbot")

user_input = st.text_input("Ask a question:")

if st.button("Submit"):
    response = chatbot(user_input)
    st.write("Chatbot:", response)

