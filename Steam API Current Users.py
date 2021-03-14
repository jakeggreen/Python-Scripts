import requests
import json
from datetime import datetime

#setup

#pull in API key from text file
APIKey_file = open('Steam API Key.txt', 'rt')
APIKey = APIKey_file.read()

#get list of company numbers from text file
App_ID_File = open('App IDs.txt', 'rt')
App_IDs = App_ID_File.read()
App_ID_List = App_IDs.split('\n')

url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/'
payload = {}
headers = {}

# https://api.steampowered.com/<interface name>/<method name>/v<version>/?key=<api key>&format=<format>
# https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/

#end setup

for App_ID in App_ID_List:
	full_url =  url + '?key=' + APIKey + '&appid=' + App_ID
	response = requests.request('GET', full_url, headers=headers, data=payload)
	game_data =  response.json()
	current_players = game_data.get('response').get('player_count')
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print(current_time + ' ' + str(current_players))
