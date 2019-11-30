import requests
from flask import current_app as app

product_path = app.config['PRODUCT_SERVICE']

class ProductClient:

    @staticmethod
    def get_product(slug):
        response = requests.request(method="GET", url=product_path+'/api/product/' + slug)
        product = response.json()
        return product

    @staticmethod
    def get_products():
        r = requests.get(product_path+'/api/products')
        products = r.json()
        return products
