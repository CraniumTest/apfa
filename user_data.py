# user_data.py
class UserData:
    def __init__(self):
        # Simulated user financial data
        self.budget = {"income": 5000, "expenses": 3000, "savings": 200}

    def get_budget_overview(self):
        return f"Your current income is {self.budget['income']} and expenses are {self.budget['expenses']}."

