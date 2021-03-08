import requests
import json

APIKey_file = open("C:/Users/jakeg/Documents/Apex.txt", "rt")
APIKey = APIKey_file.read()

legend_names = ["Bloodhound", "Gibraltar", "Lifeline", "Pathfinder", "Wraith", "Bangalore", "Caustic", "Mirage", 
"Octane", "Wattson", "Crypto", "Revenant", "Loba", "Rampart", "Horizon", "Fuse"]

url = 'https://public-api.tracker.gg/v2/apex/standard/profile/origin/'

player_name = 'majorquazar'

segment_type = 'legend'

full_url = url + player_name + "/segments" + "/" + segment_type

#+ "/sessions"

payload = {}

headers = {'TRN-Api-Key': APIKey}

response = requests.request("GET", full_url, headers=headers, data=payload)

player_data = response.json()

for legend in player_data["data"]:
	try:
		print(legend["metadata"]["name"] + " Kills: " + str(int(legend["stats"]["kills"]["value"])))
	except KeyError: 
		print(legend["metadata"]["name"] + " Kills: -")

# for legend in legend_names:
# 	print(legend)

# for items in stats["data"]["items"][0]["matches"]:
# 	print(items["metadata"]["character"]["displayValue"])
# 	print(items["metadata"]["character"]["displayValue"])
