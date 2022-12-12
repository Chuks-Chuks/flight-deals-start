import requests
import os
import dotenv


class UserData:
    def __init__(self):
        self.first_name = input("Enter your first name:\n").title()
        self.last_name = input("Enter your last name:\n").title()
        self.email = self.get_email()
        self.project_folder = os.path.expanduser('../flight-deals-start')
        dotenv.load_dotenv(os.path.join(self.project_folder, '.env'))
        self.endpoint = os.getenv('SHEET_USER_ENDPOINT')

    def get_email(self):
        email = input("Enter your email address:\n").lower()
        re_email = input("Confrim your email address:\n").lower()
        if email == re_email:
            return email
        else:
            return self.get_email()

    def add_customer_to_sheet(self):
        sheet_params = {
            'user': {
                'firstName': self.first_name,
                'lastName': self.last_name,
                'email': self.email,
            }
        }
        put_header = {
            "Authorization": os.getenv('SHEET_AUTHORIZATION')
        }

        get_response = requests.post(url=self.endpoint, json=sheet_params, headers=put_header)
        print(get_response.text)
