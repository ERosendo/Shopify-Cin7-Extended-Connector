import requests
import json


class Shopify:

    def __init__(self, username, password):
        with open("config.json") as json_data_file:
            self.data = json.load(json_data_file)
        self.username = username
        self.password = password
        self.header = None
        self.content = None
        self.next_link = None
        self.status_code = None

    def get_request(self, url):
        request_object = requests.get(url, auth=(self.username, self.password))
        self.header = request_object.headers
        self.content = json.loads(request_object.content)
        self.get_next_page()

    def delete_request(self, url):
        request_object = requests.delete(url, auth=(self.username, self.password))
        self.header = request_object.headers
        self.status_code = request_object.status_code
        self.content = json.loads(request_object.content)

    def product_request(self, url):
        self.get_request(url)
        return self.content

    def delete_product(self, product_id):
        return self.delete_request(f"{self.data['shopify']['base_url']}/admin/api/2020-10/products/{product_id}.json")

    def check_next_page(self):
        if 'next' in self.header['link']:
            return True
        else:
            return False

    def post_request(self, url, data):
        request_object = requests.post(url=url, json=data, auth=(self.username, self.password))
        return json.loads(request_object.content)

    def put_request(self, url, data):
        request_object = requests.put(url, json=data, auth=(self.username, self.password))
        self.status_code= request_object.status_code
        return json.loads(request_object.content)

    def activate_product(self, product_id):
        data = {
            "product": {
                "id": product_id,
                "status": "active"
            }
        }
        return self.put_request(f"{self.data['shopify']['base_url']}/admin/api/2020-10/products/{product_id}.json", data);

    def create_product_metafield(self, pro_price, product_id):
        data ={
            "variant":{
                "id": product_id,
                "metafields": [
                    {
                        "namespace": "global",
                        "key": "pro_price",
                        "value": int(float(pro_price) * 1000),
                        "value_type": "integer"
                    }
                ]
            }
        }
        return self.put_request(f"{self.data['shopify']['base_url']}/admin/api/2020-10/variants/{product_id}.json", data);

    def get_next_page(self):
        links = self.header['link'].split(',')
        for link in links:
            if 'next' in link:
                self.next_link = link.split(';')[0].strip()[1:-1]
                return self.next_link