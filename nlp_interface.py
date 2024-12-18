from transformers import pipeline

class NLPInterface:
    def __init__(self):
        self.model = pipeline('text-generation', model='gpt2')

    def process_input(self, user_input):
        # Simple keyword matching for demo purposes
        if "investment" in user_input:
            return "investment_advice", None
        return "unknown", None

    def generate_recommendations(self, profile, market_data):
        return "Based on your profile and current market trends, we recommend diversifying your portfolio."
