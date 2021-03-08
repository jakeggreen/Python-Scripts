import requests
import json

url = 'https://public-api.tracker.gg/v2/apex/standard/profile/origin/'

player_name = 'majorquazar'

full_url = url + player_name + "/sessions"

payload = {}

headers = {'TRN-Api-Key': '92143f6a-2a2a-4164-9597-8a253dabb5c1'}

response = requests.request("GET", full_url, headers=headers, data=payload)

# print(response.text)

json.JSONDecoder(response)

# print(type(data))