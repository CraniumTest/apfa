# main.py
from financial_advisor import FinancialAdvisor

def main():
    print("Welcome to the AI-Powered Personalized Financial Advisor (APFA)!")
    advisor = FinancialAdvisor()

    while True:
        user_input = input("\nHow can I assist you today? (Type exit to quit): ")
        if user_input.lower() == 'exit':
            print("Thank you for using APFA. Goodbye!")
            break

        response = advisor.handle_query(user_input)
        print(response)

if __name__ == "__main__":
    main()

