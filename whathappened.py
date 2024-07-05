from lookup import search_day,search_year,search_month,search_text
from inputt import request_input

def search_event():
    input_combo = request_input()
    input_type= input_combo[0]
    input_text= input_combo[1]
    print(input_type)
    if input_type=="1":
        res_text = search_text(input_text)
        return res_text
    if input_type=="2":       
        res_year=search_year(input_text)
        return res_year
    if input_type=="3":       
        res_month=search_month(input_text)
        return res_month
    if input_type=="4":       
        res_day=search_day(input_text)
        return res_day


def whathappened():
    hist_event=search_event()
    if hist_event:
        print(hist_event)
    else:
        print("Something wrong happened")



whathappened()