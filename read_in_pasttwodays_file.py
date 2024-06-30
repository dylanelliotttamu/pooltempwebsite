# read in the past_two_days_water_temp_file
with open('past_two_days_water_temp.txt', 'r') as file:
    past_two_days_water_temp = file.read()
    print('past two days water temp ', past_two_days_water_temp)