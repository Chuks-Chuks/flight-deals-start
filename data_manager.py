import requests
import os
from dotenv import load_dotenv


class DataManager:
    def __init__(self):
        self.destination_data = None
        self.project_folder = os.path.expanduser('../flight-deals-start')
        load_dotenv(os.path.join(self.project_folder, '.env'))
        self.endpoint = os.getenv('SHEET_ENDPOINT')
        self.flight_response = requests.get(url=self.endpoint)
        self.data = self.flight_response.json()
        self.prices = self.data["prices"]

    def put(self, city_code):
        put_params = {
            'price': {
                'iataCode': city_code['iataCode']
            }
        }
        put_header = {
            "Authorization": os.getenv('SHEET_AUTHORIZATION')
        }
        response = requests.put(
            url=f"{self.endpoint}/{city_code['id']}",
            json=put_params,
            headers=put_header)
