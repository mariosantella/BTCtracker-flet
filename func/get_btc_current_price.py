import requests

api_url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=EUR"

def get_price():
    response = requests.get(api_url)
    data = response.json()
    return data["BTC"]["EUR"]

