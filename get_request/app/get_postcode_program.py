import requests
import json
from pprint import pprint

class PostCode:

    def __init__(self, postcode):
        self.postcode = postcode
        self.headers = {"Content-Type": "application/json"}

    def retrieve_postcode(self):
        postcode_columns = requests.get(f"https://api.postcodes.io/postcodes/{self.postcode}")
        return dict(postcode_columns.json())["result"]

request1 = PostCode("DT9 4LS")
pprint(request1.retrieve_postcode()['admin_county'])