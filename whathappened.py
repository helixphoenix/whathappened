from search_event import search
from inputt import request_input
import json

def search_event():
    url = request_input()
    history =search(url)
    return history


def structure_result(history):
   pretty_history = sorted(history,key=lambda k: k['year'],reverse = True ) 
   return pretty_history

def whathappened():
    hist_event=search_event()
    if hist_event:
    
    #   pretty=structure_result(hist_event)  
      for date in hist_event:
        print(json.dumps(date, indent=4))
    else:
        print("Something wrong happened")



whathappened()