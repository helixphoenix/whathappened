from search_event import search
from inputt import request_input
import json

def search_event():
    url = request_input()
    history =search(url)
    return history



def print_pretty(response):
    for event in response:
        pretty=f"Date: {event['year']}/{event['month']}/{event['day']}\nWhat happened?! : {event['event']}"
        print(pretty)
    return print("His torry has been presented."  )  

def whathappened():
    hist_event=search_event()
    if hist_event:
        print_pretty(hist_event)
    else:
        print("Something wrong happened")

whathappened()