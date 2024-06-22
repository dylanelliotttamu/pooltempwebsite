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
    except:
        print('Error requesting data from NWS api')

    
# def parse_weather_data(data):
#     try:
#         # Access various elements within the JSON structure
#         context = data["@context"]
#         geometry_type = data["geometry"]["type"]
#         coordinates = data["geometry"]["coordinates"]
#         units = data["properties"]["units"]
#         forecast_generator = data["properties"]["forecastGenerator"]
#         generated_at = data["properties"]["generatedAt"]
#         update_time = data["properties"]["updateTime"]
#         valid_times = data["properties"]["validTimes"]
#         elevation = data["properties"]["elevation"]["value"]

#         # Access periods
#         periods = data["properties"]["periods"]

#         # Example of printing the temperature and short forecast for each period
#         for period in periods:
#             start_time = period["startTime"]
#             end_time = period["endTime"]
#             temperature = period["temperature"]
#             short_forecast = period["shortForecast"]
#             print(f"From {start_time} to {end_time}, the temperature is {temperature}°{period['temperatureUnit']} with a forecast of {short_forecast}.")
#     except:
#         print('Error parsing data')


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


# parse_weather_data(data)
