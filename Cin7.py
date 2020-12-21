import requests
import json


class Cin7:

    def __init__(self, username, password):
        with open("config.json") as json_data_file:
            self.data = json.load(json_data_file)
        self.username = username
        self.password = password
        self.header = None
        self.content = None

    def get_request(self, url):
        request_object = requests.get(url, auth=(self.username, self.password))
        self.header = request_object.headers
        self.content = json.loads(request_object.content)

    def product_request(self, url):
        self.get_request(url)
        return self.content

    def get_product_by_sku(self, sku):
        return self.product_request(f"{self.data['cin7']['base_url']}api/v1/Products/?where=styleCode='{sku}'")