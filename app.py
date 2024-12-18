from nlp_interface import NLPInterface
from financial_data import FinancialData
from user_profile import UserProfile

def main():
    nlp = NLPInterface()
    data = FinancialData()
    user = UserProfile()

    # Example interaction
    user_query = input("How can I help you today? ")
    intent, entities = nlp.process_input(user_query)

    if intent == "investment_advice":
        profile = user.get_profile()
        market_trends = data.fetch_market_data()
        recommendations = nlp.generate_recommendations(profile, market_trends)
        print(recommendations)

if __name__ == "__main__":
    main()
