# write the initial conditions of the water temp 

from datetime import datetime, timedelta

# define inital dates and water temps 
# first column is strings, second column is dates, third column is water temps

two_days_ago_date = datetime.now() - timedelta(days=2)
two_days_ago_water_temp = 80



one_day_ago_date = datetime.now() - timedelta(days=1)
one_day_ago_water_temp = 70


# write the dates and water temps to a file
with open('past_two_days_water_temp.txt', 'w') as file:
    file.write(f"{two_days_ago_date},{two_days_ago_water_temp}\n")
    file.write(f"{one_day_ago_date},{one_day_ago_water_temp}\n")

