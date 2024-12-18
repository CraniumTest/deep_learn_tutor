import random
from transformers import pipeline

class TutorBot:
    def __init__(self):
        # Load pre-trained chatbot model using transformers library
        self.chatbot = pipeline("conversational", model="microsoft/DialoGPT-small")
    
    def answer_query(self, user_input):
        conversation = self.chatbot(user_input)
        response = str(conversation)
        return response

    def intro_message(self):
        return "Hello! I am your AI tutor. Ask me any question, and I'm happy to help!"

