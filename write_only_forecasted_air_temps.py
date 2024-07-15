# WRITE ONLY forecasted pool temp file

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
            # humidity = period["relativeHumidity"]["value"]

            if date not in daily_data:
                # daily_data[date] = {"temperatures": [], "humidities": []}
                daily_data[date] = {"temperatures": []}
            
            daily_data[date]["temperatures"].append(temperature)
            # daily_data[date]["humidities"].append(humidity)

        
        global average_temp_list
        # global average_humidity_list
        global date_list
        global average_temp_list_rounded
        
        # store the average temperature and humidity I calculated for each day
        date_list = []
        average_temp_list = []
        # average_humidity_list = []

        # Calculate and print daily averages
        for date, data in daily_data.items():
            # avg_temperature = sum(data["temperatures"]) / len(data["temperatures"])
            print('date', date)
            print('data', data)

            avg_temperature = ( max(data["temperatures"]) + min(data["temperatures"]) ) / 2
            print('max temp ', max(data["temperatures"]))
            print('min temp ', min(data["temperatures"]))
        
            if len(data["temperatures"]) < 18:
                print('not enough data for this day, it will not be appended to average_temp_list ', date)
                continue
            

            # avg_humidity = sum(data["humidities"]) / len(data["humidities"])
            print(f"Date: {date}, Average Temperature: {avg_temperature:.2f}°F")
            # save the date also to a list
            date_list.append(date)
            average_temp_list.append(avg_temperature)
            # average_humidity_list.append(avg_humidity)
        # Round to 2 decimal places
        average_temp_list_rounded = [round(i,2) for i in average_temp_list]
        # average_humidity_list_rounded = [round(i,2) for i in average_humidity_list]
        # print('average humidity list rounded ', average_humidity_list_rounded)
        print('average temp list rounded ', average_temp_list_rounded)
        print('date list ', date_list)

    except Exception as e:
        print(f"Error parsing data: {e}")


pull_api_temp_data_main(lat, lon,1)

# write forecasted air temp file 
with open('forecasted_air_temp.txt', 'w') as file:
    for i in range(len(date_list)):
        file.write(f"{date_list[i]},{average_temp_list_rounded[i]}\n")




# two_days_ago_date = datetime.now().date() - timedelta(days=2)
# two_days_ago_air_temp = 80

# one_day_ago_date = datetime.now().date() - timedelta(days=1)
# one_day_ago_air_temp = 70

# # write the dates and air temps to a file
# with open('past_two_days_air_temp.txt', 'w') as file:
#     file.write(f"{two_days_ago_date},{two_days_ago_air_temp}\n")
#     file.write(f"{one_day_ago_date},{one_day_ago_air_temp}\n")

