import mysql.connector
import json


class ProductTable:

    def __init__(self):
        with open("config.json") as json_data_file:
            self.data = json.load(json_data_file)
        self.DbInstance = mysql.connector.connect(
            host=self.data['mysql']['host'],
            user=self.data['mysql']['user'],
            password=self.data['mysql']['password'],
            database=self.data['mysql']['db_name']
        )
        self.Cursor = self.DbInstance.cursor()

