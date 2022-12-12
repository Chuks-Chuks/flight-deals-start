import requests
import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('../flight-deals-start')
load_dotenv(os.path.join(project_folder, '.env'))


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, city):

        self.kiwi_header = {
            'apikey': os.getenv('KIWI_API_KEY')
        }
        self.kiwi_params = {
            'term': city
        }
        self.response_data = requests.get(
            url=f"{os.getenv('KIWI_ENDPOINT')}/locations/query",
            params=self.kiwi_params,
            headers=self.kiwi_header)
        # print(self.response_data.text)
        self.data = self.response_data.json()
        self.iata_code = self.data['locations'][0]['code']
        if city:
            self.response = self.iata_code
