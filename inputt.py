import time

def request_input_type():
 input_type = input("What are you after ? if you want to search historical events by text please enter 1, if year please enter 2, if month please enter month 3, if day please enter 4")
 return input_type
 

def date_validation(date):
 is_date = input (f"is your wandered date/event {date} correct ? y/n")
 return is_date 

    
def take_input_in(input_type):
 if input_type == "1":
   return input("Query text to search events by. Use keywords or short phrases for best match results.")   
 elif input_type == "2":
   return input("Please enter the date of your concern. 4-digit year (e.g. 2022). For BC/BCE years, use a negative integer (e.g. -351 for 351 BC).")
 elif input_type == "3":
    return input("Integer month (e.g. 3 for March).") 
 elif input_type == "4":
     return input("Calendar day of the month as number.")
 else:
    print( "Please enter a valid input")


def request_input():
    input_type= request_input_type()
    print(input_type)
    input_type_len = 1
    if input_type_len==len(input_type):
        user_input = take_input_in(input_type)
        is_valid = date_validation(user_input)
        print(is_valid)
        if is_valid=='y':
          input_combo=[input_type,user_input]
          print(input_combo)
          return input_combo
        else:
         request_input()