API_KEY='ASID4kyd61gVOaW/1ni44Q==LP4DESSfYaJmgmRS'

historical_events_text_url='https://api.api-ninjas.com/v1/historicalevents?text={}'
historical_events_year_url='https://api.api-ninjas.com/v1/historicalevents?year={}'
historical_events_month_url='https://api.api-ninjas.com/v1/historicalevents?month={}'
historical_events_day_url='https://api.api-ninjas.com/v1/historicalevents?day={}'

events_urls = {'1':historical_events_text_url,
               '2':historical_events_year_url,
               '3':historical_events_month_url,
               '4':historical_events_day_url }



input_request = ("What are you after dear ? Please enter: \n"
		"1 - to search historical events by text, \n"
		"2 - to search year, \n"
		"3 - to search month,  \n"
		"4 - to search day \n"
		)

text_input= "Query text to search events by. Use keywords or short phrases for best match results:"
year_input= "Please enter the date of your concern. 4-digit year (e.g. 2022). For BC/BCE years, use a negative integer (e.g. -351 for 351 BC):"
month_input= "Integer month (e.g. 3 for March):"
day_input= "Calendar day of the month as number:"
error_input= "Please enter a valid input"