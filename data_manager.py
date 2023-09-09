import requests
import os
class DataManager:

    def __init__(self):
        self.sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
        self.response = requests.get(url=self.sheety_endpoint)
    def return_row(self):
        return self.response.json()

