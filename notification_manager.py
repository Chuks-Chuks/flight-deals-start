# import requests
import os
import dotenv
from twilio.rest import Client

project_folder = os.path.expanduser('../flight-deals-start')
dotenv.load_dotenv(os.path.join(project_folder, '.env'))

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
MY_NUMBER = os.getenv('TWILIO_NUMBER')
RECIEVE_NUMBER = os.getenv('MY_NUMBER')
client = Client(account_sid, auth_token)


class NotificationManager:
    def __init__(self, our_price, obtained_price, date_from, date_to, travel_from, travel_to):
        self.date_from = date_from
        self.date_to = date_to
        self.travel_from = travel_from
        self.travel_to = travel_to
        self.our_price = our_price
        self.obtained_price = obtained_price
        if self.obtained_price < self.our_price:
            client.messages \
                .create(
                    body=f"Low price alert!! Only £{self.obtained_price} to fly from {self.travel_from.title()} to "
                         f"{self.travel_to.title()} from {self.date_from} to {self.date_to}",
                    from_=MY_NUMBER,
                    to=RECIEVE_NUMBER,
                )

