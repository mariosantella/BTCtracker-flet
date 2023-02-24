import requests
import json
    
class GetWalletBalance:
    def __init__(self, address_list):
        self.address_list = address_list
        self.balance = 0
    
    # get the balance of the every address appending the string to the url "https://api.blockcypher.com/v1/btc/main/addrs/"
    def get_balance(self):
        for address in self.address_list:
            url = "https://api.blockcypher.com/v1/btc/main/addrs/" + address
            response = requests.get(url)
            data = response.json()
            self.balance += data[0]["final_balance"]
        return data


### DUMMY --> APIs SUCKS 
"""
class GetWalletInfo:
    # this class will give a random balance in BTC for testing purposes
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
        self.api_url = "https://blockchain.info/q/addressbalance/" + self.wallet_address

    def get_balance(self):
        #random balance from 0 to 2 BTC, float with 4 decimals
        balance = random.uniform(0, 2)
        balance = round(balance, 4)
        return balance
    
    def get_balance_btc(self):
        #random balance from 0 to 2 BTC, float with 4 decimals
        balance = random.uniform(0, 2)
        balance = round(balance, 4)
        return balance

"""
