class Feedback:
    def generate_feedback(self, student_response):
        # Simple feedback based on keyword detection in response
        if "understand" in student_response.lower():
            return "Great! Keep up the good work!"
        elif "confused" in student_response.lower():
            return "It seems like you encountered some difficulties. Let's review this material again."
        else:
            return "You're making progress. Continue to the next module."

