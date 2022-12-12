import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from datetime import timedelta


program_folder = os.path.expanduser('../flight-deals-start')
load_dotenv(os.path.join(program_folder, '.env'))


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, destination):
        self.today = datetime.now()
        self.stripped_date = self.today.strftime("%d/%m/%Y")
        self.six_months = (timedelta(days=180) + self.today).strftime("%d/%m/%Y")
        self.two_days = (timedelta(days=4) + self.today).strftime("%d/%m/%Y")
        self.search_response = requests.get(
            url=f"{os.getenv('KIWI_ENDPOINT')}/v2/search",
            params={
                'fly_from': "LON",
                'fly_to': destination,
                'date_from': self.stripped_date,
                'date_to': self.two_days,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                'curr': 'GBP',
                "flight_type": "round",
            },
            headers={
                'apikey': os.getenv('kiwi_api_key')
            }
        )
        self.data = self.search_response.json()
        print(self.data)
        self.city_from = f"{self.data['data'][0]['cityFrom']}-{self.data['data'][0]['flyFrom'].upper()}"
        self.fly_from = self.data['data'][0]['flyFrom']
        self.city_to = f"{self.data['data'][0]['cityTo']}-{self.data['data'][0]['flyTo'].upper()}"
        self.fly_to = self.data['data'][0]['flyTo']
        self.price = self.data['data'][0]['conversion']["GBP"]


flight = FlightData('DPS')
