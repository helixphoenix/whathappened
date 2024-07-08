import requests 
import json
from config import API_KEY

def search(url):
    response = requests.get(url, headers={'X-Api-Key':API_KEY})
    if response.status_code == requests.codes.OK:
        result=json.loads(response.text)
        return result
    else:
        return "The history is not written yet."      