"""
This program fetches weather forecast data from the National Weather Service (NWS) and creates a csv file called 'forecast_data.csv'.
The csv file contains the seven day forecast and includes the date, max and min temperatures (F), and precipitation (1 for yes, 0 for no).
"""
import os
import json # Dump to JSON to work with website
import csv
import requests
from datetime import datetime

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Use this directory to form the path of the output file
output_file_path = os.path.join(script_dir, 'forecast_data.csv')

def get_forecast_weather():
    """
    Fetch weather forecast data from NWS for Boise location grid points latitude 133, longitude 84.

    Returns:
    dict: A dictionary containing weather forecast data if the request was successful; None otherwise.

    Raises:
    Prints an error message and returns 'None' if the API request fails.
    """
   
    endpoint = 'https://api.weather.gov/gridpoints/BOI/133,84/forecast' # endpoint for Boise location
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json() # Return the parsed JSON response as a dictionary if the request is successful
    else:
        print(f"Error fetching forecast data: {response.status_code}")
        print(f"Response Text: {response.text}")
        return None

def process_forecast(forecast_data):
    """
    Process the forecast data received from the NWS API for a specific Boise location. The function parses data 
    structured with date/time, temperature, and forecast details.

    Example data structure:
        Date/Time: 2023-11-24T06:00:00-07:00 to 2023-11-24T18:00:00-07:00
        Temperature: 42°F
        Short Forecast: Sunny
        Detailed Forecast: Sunny, with a high near 42.
    
    Parameters:
    forecast_data (dict): A dictionary containing the forecast data from the NWS API.

    Returns:
    dict: A dictionary mapping each date to its forecast details, including maximum temperature (max_temp),
          minimum temperature (min_temp), and a precipitation flag (0 for no precipitation, 1 for precipitation).
          The data is an approximation based on keywords found in the detailed forecast.
    """
    daily_forecast = {}  # Dictionary to store weather forecast data
    
    for period in forecast_data['properties']['periods']:  # Iterate over each period in the 'periods' list within the 'properties' dictionary of the forecast data
        date = datetime.fromisoformat(period['startTime']).date()   # Convert the 'startTime' from ISO 8601 format to a Python date object, extracting only the date component
        temp = period['temperature']  # Get the temperature value for the period
        forecast = period['detailedForecast'].lower()  # Convert the detailed forecast to lowercase for easier parsing

        # Initialize the dictionary for the date if it's not already present
        if date not in daily_forecast:
            daily_forecast[date] = {'max_temp': None, 'min_temp': None, 'precipitation': 0}

        # Determine if it's a high or low temperature forecast
        if 'high near' in forecast:
            daily_forecast[date]['max_temp'] = temp
        elif 'low around' in forecast:
            daily_forecast[date]['min_temp'] = temp

        # Check for keywords indicating precipitation
        if any(word in forecast for word in ['rain', 'snow', 'showers', 'precipitation']):
                daily_forecast[date]['precipitation'] = 1

    return daily_forecast

def rain_forecast():
    """
    If precipitation is found in the forecast, pull the grid data for Boise and calculate total forecasted precipitation in mm.
    Precipitation includes precipitation, ice accumulation, and snowfall.

    Example data structure:
        "quantitativePrecipitation": {
            "uom": "wmoUnit:mm",
            "values": [
                {
                    "validTime": "2023-11-20T04:00:00+00:00/PT2H",
                    "value": 0
                },  

    Returns:
    dict: A dictionary mapping each date to its precipitation forecast details in mm.
    """
    precipitation_endpoint = 'https://api.weather.gov/gridpoints/BOI/133,84' # endpoint to pull precipitation in mm
    precip_response = requests.get(precipitation_endpoint)
    if precip_response.status_code == 200:
        precip_data = precip_response.json() # Return the parsed JSON response as a dictionary if the request is successful
        daily_precipitation = {} 
        # Get the total anticipated precipitation in mm
        for period in precip_data['properties']['quantitativePrecipitation']['values']:
            date = datetime.fromisoformat(period['validTime'].split('/')[0]).date() 
            precip_value = period['value']
            if date not in daily_precipitation:
                daily_precipitation[date] = 0
            daily_precipitation[date] += precip_value
        # Get the total ice accumulation in mm  
        for period in precip_data['properties']['iceAccumulation']['values']:
            date = datetime.fromisoformat(period['validTime'].split('/')[0]).date() 
            precip_value = period['value']
            if date not in daily_precipitation:
                precip_value = 0 # Set the amount to be added to 0
            daily_precipitation[date] += precip_value      
        # Get the total snowfall amount in mm  
        for period in precip_data['properties']['snowfallAmount']['values']:
            date = datetime.fromisoformat(period['validTime'].split('/')[0]).date() 
            precip_value = period['value']
            if date not in daily_precipitation:
                precip_value = 0 # Set the amount to be added to 0
            daily_precipitation[date] += precip_value                                           
        return daily_precipitation
    else:
        print(f"Error fetching forecast data: {precip_response.status_code}")
        print(f"Response Text: {precip_response.text}")
        return None


forecast_data = get_forecast_weather() # Get the weather forecast data
precipitation_totals = rain_forecast()

if forecast_data:
    daily_forecast = process_forecast(forecast_data) # Process the forecast data
    for date in daily_forecast:
        if date in precipitation_totals:
            daily_forecast[date]['precipitation'] = precipitation_totals[date]

    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Add headers to the forecast csv file
        writer.writerow(['Date', 'Max Temperature (F)', 'Min Temperature (F)', 'Precipitation (mm)'])

        # Write the forecast data to the csv file
        for date, data in daily_forecast.items():
            writer.writerow([date, data['max_temp'], data['min_temp'], data['precipitation']])

    # Convert datetime.date objects to strings for JSON serialization
    json_ready_forecast = {str(date): data for date, data in daily_forecast.items()}

    # Convert the data to JSON and print it to work with the website
    print(json.dumps(json_ready_forecast))

    # print("Forecast data written to forecast_data.csv")
