from flask import session
from flask import current_app as app
import os
import requests

user_path = os.getenv('USER_SERVICE')

class UserClient:

    @staticmethod
    def get_user(api_key):
        headers = {
            'Authorization': api_key
        }

        response = requests.request(method="GET", url=user_path+'/api/user', headers=headers)
        if response.status_code == 401:
            return False

        user = response.json()
        return user
