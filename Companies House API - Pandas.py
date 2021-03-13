import requests
import json
import pandas as pd

#setup

#pull in API key from text file
APIKey_file = open('Companies House Key.txt', 'rt')
APIKey = APIKey_file.read()

#get list of company numbers from text file
CompanyNumber_file = open('Company Numbers.txt', 'rt')
company_file = CompanyNumber_file.read()
company_number = company_file.split('\n')

url = 'https://api.company-information.service.gov.uk/company/' 

payload = {}

headers = {'Authorization': APIKey}

companies_house_data = list();

#end setup

for company in company_number:
	# parameters = {'register_view': 'true', 'register_type': 'directors'}
	full_url = url + company + '/officers'
	response = requests.request('GET', full_url, headers=headers, data=payload)
	company_officers = response.json()
	company = company
	for name in company_officers.get('items'):
		if not name.get('resigned_on') and name.get('officer_role') == 'director':
			try:
				API_name = name['name'] #takes the name in the API formatted (surname, first_names other_names)
				temp_name = API_name.replace(',','') #removes the comma from the API name format
				end = len(temp_name) #finds the length of the full name
				surname_end_location = temp_name.find(' ') #finds the location of the end of the surname
				surname = temp_name[0:surname_end_location] #sets the surname
				other_names = temp_name[surname_end_location + 1:end] #sets the other names
				officer = other_names.upper() + ' ' + surname.upper() #creates new name
				companies_house_data.append([company, officer])
			except ValueError:
				pass		

ch_excel_data = pd.DataFrame(companies_house_data,
                   columns=['Company', 'Officer'])
print(ch_excel_data)
ch_excel_data.to_excel (r'companies_house_data.xlsx', index = False, header=True)