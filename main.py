from tutor_bot import TutorBot
from learning_path import LearningPath
from utils.feedback import Feedback


def main():
    tutor_bot = TutorBot()
    learning_path = LearningPath()
    feedback_system = Feedback()
    
    # Display intro message
    print(tutor_bot.intro_message())
    
    # Example student input
    student_input = "Can you help me understand neural networks?"
    tutor_response = tutor_bot.answer_query(student_input)
    print(f"AI Tutor: {tutor_response}")
    
    # Generate personalized learning path
    content = learning_path.personalize_content()
    print(f"Personalized learning content recommended: {content}")
    
    # Simulated student response
    student_response = "I understand the basics now."
    feedback = feedback_system.generate_feedback(student_response)
    print(f"Feedback: {feedback}")

if __name__ == "__main__":
    main()

