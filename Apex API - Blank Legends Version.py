import requests
import json

APIKey_file = open("C:/Users/jakeg/Documents/Apex.txt", "rt")
APIKey = APIKey_file.read()

url = 'https://public-api.tracker.gg/v2/apex/standard/profile/'

player_name = 'majorquazar'

platform_name = 'origin'

segment_type = 'legend'

full_url = url + platform_name + "/" + player_name + "/segments" + "/" + segment_type

payload = {}

headers = {'TRN-Api-Key': APIKey}

response = requests.request("GET", full_url, headers=headers, data=payload)

player_data = response.json()

legend_names = ["Bloodhound", "Gibraltar", "Lifeline", "Pathfinder", "Wraith", "Bangalore", "Caustic", "Mirage", 
"Octane", "Wattson", "Crypto", "Revenant", "Loba", "Rampart", "Horizon", "Fuse"]

API_legend_name = []

for name in player_data["data"]:
	name = name["metadata"]["name"]
	API_legend_name.append(name)

print(legend_names)
print(API_legend_name)

for legend in legend_names:
	for APIlegend in API_legend_name:
		if legend == APIlegend:
			for legend_stats in player_data["data"]:
				try:
					print(legend + " Kills: " + str(int(legend_stats["stats"]["kills"]["value"])))
				except KeyError: 
					print(legend + " Kills: -")
		else:
			print(legend)
