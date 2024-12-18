class UserProfile:
    def __init__(self):
        self.profile = {
            "income": 50000,
            "expenses": 20000,
            "goals": "retirement",
            "risk_tolerance": "medium"
        }

    def get_profile(self):
        return self.profile
