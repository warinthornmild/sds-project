import requests
import os

PRODUCT_SERVICE = os.getenv('PRODUCT_SERVICE')

class ProductClient:

    @staticmethod
    def get_product(slug):
        response = requests.request(method="GET", url=PRODUCT_SERVICE+'/api/product/' + slug)
        product = response.json()
        return product

    @staticmethod
    def get_products():
        r = requests.get(PRODUCT_SERVICE+'/api/products')
        products = r.json()
        return products
