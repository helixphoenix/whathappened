import requests
from config import API_KEY, events_urls
date = '-618'
api_url = events_urls['2'].format(date)
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
print(response)
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
