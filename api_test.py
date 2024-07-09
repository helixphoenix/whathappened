import requests
import json
from config import API_KEY, events_urls


date ='roman empire'
api_url = events_urls['1'].format(date)
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
if response.status_code == requests.codes.ok:
   print_pretty(response.text)
else:
    print("Error:", response.status_code, response.text)




