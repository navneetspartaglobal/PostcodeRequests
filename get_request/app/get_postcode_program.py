import requests
import json
# post_code_request = requests.get("https://api.postcodes.io/postcodes/se120nb")
#
# print(post_code_request.status_code)
# print(post_code_request.headers)
#
# print(type(post_code_request.content))


json_body = json.dumps({"postcodes":[" UB1 2ST", "UB4 0PZ", "UB1 3LX"]})

headers = {"Content-type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)


print(post_multi_req.json())