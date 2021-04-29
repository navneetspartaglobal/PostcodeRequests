import requests
import json
from pprint import pprint


class PostCode:
    def __init__(self, postcode):
        self.postcode = postcode
        self.headers = {"Content-Type": "application/json"}

    def retrieve_postcode(self, column_list):
        postcode_columns = requests.get(f"https://api.postcodes.io/postcodes/{self.postcode}")
        outlist = []
        [outlist.append(dict(postcode_columns.json())["result"][column]) for column in column_list]
        return outlist

request1 = PostCode("DT9 4LS")
pprint(request1.retrieve_postcode(['admin_county', 'region']))


"""
json_body = json.dumps({"postcodes":["HP226DB"]})
headers = {"Content-Type":"application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

postcode_dictionary = dict(post_multi_req.json()["result"][0]["result"]).items()
key_list = [k for (k, v) in postcode_dictionary]
print(list)
"""
