from flask import session
from flask import current_app
import requests
import os

ORDER_SERVICE = os.getenv('ORDER_SERVICE')

class OrderClient:

    @staticmethod
    def get_order():
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }

        response = requests.request(method="GET", url=ORDER_SERVICE+'/api/order', headers=headers)
        order = response.json()
        return order

    @staticmethod
    def update_order(items):

        url = ORDER_SERVICE+'/api/order/update'
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        response = requests.request("POST", url=url, data=items, headers=headers)
        if response:
            order = response.json()

            return order

    @staticmethod
    def post_add_to_cart(product_id, qty=1):
        payload = {
            'product_id': product_id,
            'qty': qty,
        }
        url = ORDER_SERVICE+'/api/order/add-item'
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        response = requests.request("POST", url=url, data=payload, headers=headers)
        if response:
            order = response.json()

            return order

    @staticmethod
    def post_checkout():
        url = ORDER_SERVICE+'/api/order/checkout'
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        response = requests.request("POST", url=url, data={}, headers=headers)
        order = response.json()
        return order

    @staticmethod
    def get_order_from_session():
        default_order = {
            'items': {},
            'total': 0,
        }
        return session.get('order', default_order)


