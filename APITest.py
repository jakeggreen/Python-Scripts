import requests
import json

APIKey_file = open("C:/Users/jakeg/Documents/Apex.txt", "rt")
APIKey = APIKey_file.read()

url = 'https://public-api.tracker.gg/v2/apex/standard/profile/origin/'

player_name = 'majorquazar'

segment_type = 'legend'

full_url = url + player_name + "/segments" + "/" + segment_type

#+ "/sessions"

payload = {}

headers = {'TRN-Api-Key': APIKey}

response = requests.request("GET", full_url, headers=headers, data=payload)

player_data = response.json()

for name in player_data["data"]:

	try:
		print(name["metadata"]["name"] + " Kills: " + str(int(name["stats"]["kills"]["value"])))
	except KeyError: 
		print(name["metadata"]["name"] + " Kills: -")

# for items in stats["data"]["items"][0]["matches"]:
# 	print(items["metadata"]["character"]["displayValue"])
# 	print(items["metadata"]["character"]["displayValue"])
