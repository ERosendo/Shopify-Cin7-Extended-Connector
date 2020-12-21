import json
from DataBase import ProductTable
from Shopify import Shopify
from Cin7 import Cin7

with open("config.json") as json_data_file:
    data = json.load(json_data_file)


ShopifyConnector = Shopify(data['shopify']['username'], data['shopify']['password'])
Cin7Connector = Cin7(data['cin7']['username'], data['cin7']['password'])




