import requests

class FinancialData:
    def __init__(self):
        self.api_key = 'YOUR_API_KEY'

    def fetch_market_data(self):
        # Example using Alpha Vantage API
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        return data
