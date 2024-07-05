import requests



API_KEY='ASID4kyd61gVOaW/1ni44Q==LP4DESSfYaJmgmRS'


    

historical_events_text_url='https://api.api-ninjas.com/v1/historicalevents?text={}'

def search_text (text):
    build_search_url=historical_events_text_url.format(text)
    print(build_search_url)
    response = requests.get(build_search_url, headers={'X-Api-Key':API_KEY})
    print(response)
    if response.status_code == requests.codes.OK:
        return response.text
    else:
        return "The history is not written yet."        
    

historical_events_year_url='https://api.api-ninjas.com/v1/historicalevents?year={}'


def search_year (year):
    build_search_url=historical_events_year_url.format(year)
    print(build_search_url)
    response = requests.get(build_search_url, headers={'X-Api-Key':API_KEY})
    print(response)
    if response.status_code == requests.codes.OK:
        return response.text
    else:
        return "The year is not written yet."    
    
    
historical_events_month_url='https://api.api-ninjas.com/v1/historicalevents?month={}'


def search_month (month):
    build_search_url=historical_events_month_url.format(month)
    response = requests.get(build_search_url, headers={'X-Api-Key':API_KEY})
    if response.status_code == requests.codes.OK:
        return response.text
    else:
        return "The month is not written yet."    
    
    
    
historical_events_day_url='https://api.api-ninjas.com/v1/historicalevents?day={}'


def search_day (day):
    build_search_url=historical_events_day_url.format(day)
    response = requests.get(build_search_url, headers={'X-Api-Key':API_KEY})
    if response.status_code == requests.codes.OK:
        return response.text
    else:
        return "The day is not written yet."    
    

