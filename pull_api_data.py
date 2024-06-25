# Python script to pull NWS api data from selected station

# Import necessary libraries
import numpy as np
import urllib.request
import json
from datetime import datetime


lat , lon = 88, 58

#frequency this script is ran will be determined by another script that will call this one

# Main function to pull data from NWS api
def pull_api_temp_data_main(lat, lon,timestep_in_hours):
    try:
        # pull data from NWS api
        if timestep_in_hours == 1:
            url_hourly = f'https://api.weather.gov/gridpoints/SGX/{lat},{lon}/forecast/hourly' 

            request_data(url_hourly)

            parse_weather_data(data)
            
        else:
            print('Invalid timestep')
    except:
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

        # Calculate and print daily averages
        for date, data in daily_data.items():
            avg_temperature = sum(data["temperatures"]) / len(data["temperatures"])
            avg_humidity = sum(data["humidities"]) / len(data["humidities"])
            print(f"Date: {date}, Average Temperature: {avg_temperature:.2f}°F, Average Humidity: {avg_humidity:.2f}%")

        


    except Exception as e:
        print(f"Error parsing data: {e}")



pull_api_temp_data_main(lat, lon, timestep_in_hours=1)


# now i should have objects that I can have the lambda handler use to display the data

# create a text file to store the data for the html page to use
# with open('data.txt', 'w') as f:
#     f.write(data)



water_temp_1_day_ago = 80
water_temp_2_days_ago = 78


today_water_temperature = (water_temp_1_day_ago + water_temp_2_days_ago ) / 2



