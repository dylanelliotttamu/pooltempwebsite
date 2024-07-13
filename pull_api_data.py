# Python script to pull NWS api data from selected station

# Import necessary libraries
import numpy as np
import urllib.request
import json
from datetime import datetime
from datetime import date, timedelta


lat, lon = 31.6212, -97.0037 # Waco, TX

def fetch_json_from_url(url):
    with urllib.request.urlopen(url) as response:
        global data_1
        data_1 = json.loads(response.read().decode())
        # print(data_1)
        return data_1
    
def get_hourly_forecast_url(input_data):
    try:
        global hourly_forecast_url
        hourly_forecast_url = input_data["properties"]["forecastHourly"]
        return hourly_forecast_url
    except KeyError as e:
        print(f"KeyError: {e}")

#given lat, lon of a wave pool (US), retrieve the hourly forecast link
def retrieve_the_hourly_url_given_only_lat_and_lon(input_lat,input_lon):
    fetch_json_from_url(f'https://api.weather.gov/points/{input_lat},{input_lon}')
    get_hourly_forecast_url(data_1)
    
    return hourly_forecast_url



#frequency this script is ran will be determined by another script that will call this one

# Main function to pull data from NWS api
def pull_api_temp_data_main(lat, lon,timestep_in_hours):
    try:
        # pull data from NWS api
        if timestep_in_hours == 1:
            # url_hourly = f'https://api.weather.gov/gridpoints/SGX/{lat},{lon}/forecast/hourly' 
            
            retrieve_the_hourly_url_given_only_lat_and_lon(lat,lon)
            # print('hourly_forecast_url ',hourly_forecast_url)
            request_data(hourly_forecast_url)

            parse_weather_data(data)

        else:
            print('Invalid timestep')

    
    except KeyError as e:
        print(f"KeyError: {e}")
        print('Error pulling data from NWS api')
    

# Use url and return data 
def request_data(url):
    try:
        with urllib.request.urlopen(url) as response: #url:
            #data = json.loads(url.read().decode())
            global data
            data = json.loads(response.read().decode())
            return data 
            # returns 7-days of hourly data
    except Exception as e:
        print(f"Error requesting data: {e}")


def parse_weather_data(data):
    try:  
        # Access periods
        periods = data["properties"]["periods"]
        
        # Dictionary to hold aggregated data by day
        global daily_data
        daily_data = {}

        for period in periods:
            start_time = period["startTime"]
            date = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S%z").date()
            temperature = period["temperature"]
            humidity = period["relativeHumidity"]["value"]

            if date not in daily_data:
                daily_data[date] = {"temperatures": [], "humidities": []}
            
            daily_data[date]["temperatures"].append(temperature)
            daily_data[date]["humidities"].append(humidity)

        # store the average temperature and humidity I calculated for each day
        global average_temp_list
        global average_humidity_list
        global date_list

        date_list = []
        average_temp_list = []
        average_humidity_list = []

        # Calculate and print daily averages
        for date, data in daily_data.items():
            avg_temperature = sum(data["temperatures"]) / len(data["temperatures"])
            avg_humidity = sum(data["humidities"]) / len(data["humidities"])
            print(f"Date: {date}, Average Temperature: {avg_temperature:.2f}°F")
            # save the date also to a list
            date_list.append(date)
            average_temp_list.append(avg_temperature)
            average_humidity_list.append(avg_humidity)
        # Round to 2 decimal places
        average_temp_list_rounded = [round(i,2) for i in average_temp_list]
        average_humidity_list_rounded = [round(i,2) for i in average_humidity_list]
        # print('average humidity list rounded ', average_humidity_list_rounded)
        print('average temp list rounded ', average_temp_list_rounded)
        print('date list ', date_list)

    except Exception as e:
        print(f"Error parsing data: {e}")


'''

Begin main part of script and call functions

'''
# Process:
# If new day: 
# Read in past2days air temp file and replace date and associated temp of 1day ago to 2 day ago
# Read in forecasted air temp file and take the 1st entry and replace with 1 day ago
# Then run the rest of the script


# Read the file
with open('past_two_days_air_temp.txt', 'r') as file:
    lines = file.readlines()
    # print('lines ',lines)

# Parse the data
two_days_ago_date_in_past_two_days_air_temp_file, two_days_ago_air_temp_in_past_two_days_air_temp_file = lines[0].strip().split(',')
one_day_ago_date_in_past_two_days_air_temp_file, one_day_ago_air_temp_in_past_two_days_air_temp_file = lines[1].strip().split(',')

print('Two days ago:')
print(f"Date: {two_days_ago_date_in_past_two_days_air_temp_file}, Air Temp: {two_days_ago_air_temp_in_past_two_days_air_temp_file}")

print('One day ago:')
print(f"Date: {one_day_ago_date_in_past_two_days_air_temp_file}, Air Temp: {one_day_ago_air_temp_in_past_two_days_air_temp_file}")

# Read the forecasted air temp file
with open('forecasted_air_temp.txt', 'r') as file:
    forecasted_air_temp = file.read()
    # print('forecasted air temp ', forecasted_air_temp)






# # read in the past_two_days_air_temp_file
# with open('past_two_days_air_temp.txt', 'r') as file:
#     past_two_days_air_temp = file.read()
#     print('past two days air temp read file = ', past_two_days_air_temp)

# # the way I wrote it, the first entry should be "two days ago" date and have the air temp from "two days ago"

# # set the first date and air temp from the past_two_days_air_temp file
# two_days_ago_date_in_past_two_days_air_temp_file = past_two_days_air_temp.split(',')[0]
# two_days_ago_air_temp_in_past_two_days_air_temp_file = past_two_days_air_temp.split(',')[1]
# one_day_ago_date_in_past_two_days_air_temp_file = past_two_days_air_temp.split(',')[2]

# print('one_dayago date', one_day_ago_date_in_past_two_days_air_temp_file)


# one_day_ago_air_temp_in_past_two_days_air_temp_file = past_two_days_air_temp.split(',')[3]



# print('first date in forecasted pool temp file ', two_days_ago_date_in_past_two_days_air_temp_file)
# print('first date air temp in forecasted pool temp file ', two_days_ago_air_temp_in_past_two_days_air_temp_file)


# print('one day ago air temp in past two days air temp file ', one_day_ago_air_temp_in_past_two_days_air_temp_file)




    


# # # Call the main function
# # pull_api_temp_data_main(lat, lon, timestep_in_hours=1)

# # print('len average_temp_list ',len(average_temp_list))
# # print('len date_list',len(date_list))

# # # Now I have average air temp list and date list
# # # Now I need to calculate the average water temperature for each day
# # # I use average air temp past 2 days to calculate the average water temperature for today

# # #retrieve the water temperature for the past 2 days

# # # READ FILE past_two_days_water_temp.txt
# # with open('past_two_days_water_temp.txt', 'r') as file:
# #     past_two_days_water_temp = file.read()
# #     print('past two days water temp ', past_two_days_water_temp)


