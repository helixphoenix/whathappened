import time
from config import events_urls, input_request, text_input,year_input,month_input,day_input, error_input


def request_input_type():
 input_type = input(input_request)
 return input_type
 

def date_validation(date):
 is_date = input (f"is your wandered event/year/month/day {date} correct ? y/n")
 return is_date 

    
def take_input_in(input_type):
 if input_type == "1":
   return input(text_input)   
 elif input_type == "2":
   return input(year_input)
 elif input_type == "3":
    return input(month_input) 
 elif input_type == "4":
     return input(day_input)
 else:
    print(error_input)

    


def request_input():
    input_type= request_input_type()
    input_type_len = 1
    if input_type_len==len(input_type):
        user_input = take_input_in(input_type)
        is_valid = date_validation(user_input)
        if is_valid=='y':
          url =events_urls[input_type].format(user_input)
          return url
        else:
         request_input()