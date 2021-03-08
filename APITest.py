import requests
import json

url = 'https://public-api.tracker.gg/v2/apex/standard/profile/origin/'

player_name = 'majorquazar'

segment_type = 'legend'

full_url = url + player_name + "/segments" + "/" + segment_type

#+ "/sessions"

payload = {}

headers = {'TRN-Api-Key': '92143f6a-2a2a-4164-9597-8a253dabb5c1'}

response = requests.request("GET", full_url, headers=headers, data=payload)

player_data = response.json()

for name in player_data["data"]:

	try:
		print(name["metadata"]["name"]), print("Kills: " + str(int(name["stats"]["kills"]["value"])))
	except KeyError: 
		print("No data")

# for items in stats["data"]["items"][0]["matches"]:
# 	print(items["metadata"]["character"]["displayValue"])
# 	print(items["metadata"]["character"]["displayValue"])