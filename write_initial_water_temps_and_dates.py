# to write the initial conditions of the air temp and dates

from datetime import datetime, timedelta

# define inital dates and air temps 
# first column is strings, second column is dates, third column is air temps

# use datetime.now() but only for the date, not the time =.date()
two_days_ago_date = datetime.now().date() - timedelta(days=2)
two_days_ago_air_temp = 80

one_day_ago_date = datetime.now().date() - timedelta(days=1)
one_day_ago_air_temp = 70

# write the dates and air temps to a file
with open('past_two_days_air_temp.txt', 'w') as file:
    file.write(f"{two_days_ago_date},{two_days_ago_air_temp}\n")
    file.write(f"{one_day_ago_date},{one_day_ago_air_temp}\n")

