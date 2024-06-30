from datetime import datetime, timedelta

# read in the past_two_days_air_temp_file
with open('past_two_days_air_temp.txt', 'r') as file:
    past_two_days_air_temp = file.read()
    print('past two days air temp ', past_two_days_air_temp)

# set the first date and air temp from the past_two_days_air_temp file
first_date_in_past_two_days_air_temp_file = past_two_days_air_temp.split(',')[0]
first_date_air_temp_in_past_two_days_air_temp_file = past_two_days_air_temp.split(',')[1]


# first_date_in_forecasted_pool_temp_file should be "two days ago" date and have the air temp from "two days ago"

print('first date in historical', first_date_air_temp_in_past_two_days_air_temp_file)
print('first date air temp in forecasted pool temp file ', first_date_air_temp_in_past_two_days_air_temp_file)


