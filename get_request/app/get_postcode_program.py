import requests
import json
from pprint import pprint


class PostCode:
    def __init__(self, post_code, columns):
        self.postcode = post_code
        self.column_list = columns

    def retrieve_postcode_details(self):
        postcode_details = requests.get(f"https://api.postcodes.io/postcodes/{self.postcode}")
        return dict(postcode_details.json())["result"].items()

    def select_values(self):
        postcode_details_dictionary = self.retrieve_postcode_details()
        return [(key, value) for (key, value) in postcode_details_dictionary if key in self.column_list]


request1 = PostCode("DT9 4LS", ['postcode', 'quality', 'eastings', 'northings', 'country', 'nhs_ha', 'longitude', 'latitude', 'european_electoral_region', 'primary_care_trust', 'region', 'lsoa', 'msoa', 'incode', 'outcode'])
pprint(request1.select_values())