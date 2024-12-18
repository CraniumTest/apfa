# financial_advisor.py
from user_data import UserData

class FinancialAdvisor:
    def __init__(self):
        self.user_data = UserData()

    def handle_query(self, query):
        # Simulate a simple response generation
        if "budget" in query.lower():
            return self.user_data.get_budget_overview()
        elif "investment" in query.lower():
            return "Here's an overview of popular investment options based on current trends."
        else:
            return "I'm here to help with your finances. Please ask about budgeting, investments, or planning."

    def personalize_advice(self, user_profile):
        # Placeholder for personalized advice generation
        return "Based on your profile, I would recommend setting a savings goal of 10% monthly income."

