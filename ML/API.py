"""
NOAA API to fetch historical weather data.
This program fetches historical maximum and minimum temperatures and precipitation from 2020 through the current year and creates a csv file called 'historical_weather.csv'.
The csv file contains the historical weather data for the specified period and includes the date, max and min temperatures (F), and precipitation (mm).
"""
import csv
import requests
from datetime import datetime

def get_historical_weather(api_key, start_date, end_date, datasetid, stationid, datatype, units="standard"):
    """
    Fetch historical weather data from NOAA.

    Parameters:
    api_key (str): API token for authenticatin with NOAA.
    start_date (str): The start date for the data query in 'YYYY-MM-DD' format.
    end_date (str): The end date for the data query in 'YYYY-MM-DD' format.
    datasetid (str): The identifier for the dataset to query. Example: 'GHCND' for Daily Summaries.
    stationid (str): The identifier for the observation station. Example: 'GHCND:USW00024131'.
    datatype (str): The type of data to fetch. Example: 'TMAX' for maximum temperature.
    units (str): The units for the results ('standard' or 'metric').

    Returns:
    A dictionary with the weather data if the request was successful; None otherwise.

    Raises:
    Prints an error message and returns 'None' if the API request fails.
    """
   
    endpoint = 'https://www.ncei.noaa.gov/cdo-web/api/v2/data'

    params = {
        'datasetid':datasetid,
        'stationid':stationid,
        'datatypeid':datatype,
        'startdate':start_date,
        'enddate':end_date,
        'units':units,
        'limit':1000,
    }

    headers = {
        'token':api_key
    }

    response = requests.get(endpoint, headers=headers, params=params)

    # Print error details upon failure
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        print(f"Request URL: {response.url}") 
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Text: {response.text}")
        return None

# Fetch the data and append it to a dictionary
def fetch_data(year, api_key, datasetid, stationid, datatypeid):
    """
    Fetch and combine historical weather data for a given year from NOAA.

    Parameters:
    year (int): The year for which to fetch weather data.
    api_key (str): API token for authenticatin with NOAA.
    datasetid (str): The identifier for the dataset to query. Example: 'GHCND' for Daily Summaries.
    stationid (str): The identifier for the observation station. Example: 'GHCND:USW00024131'.
    datatypeids (list): A list of data type identifiers. Eample: ['TMAX', 'TMIN', 'PRCP']) for which to fetch data.

    Returns:
    dict: A dictionary with dates as keys and another dictionary as values that contains 'TMAX', 'TMIN', and 'PRCP'
          as keys with corresponding weather data as values.
    """
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    combined_results = {} # Dictionary to hold results
    
    for datatype in datatypeid: # loop through TMAX, TMIN, PRCP datatypeid
        data = get_historical_weather(api_key, start_date, end_date, datasetid, stationid, datatype) # Retrieve weather data for the datatype
        if data and "results" in data: # if data is not 'None' and 'results' are found
            for item in data["results"]: # go through each date and find the data (e.g. max temp on 1/1/23)
                date = item["date"].split("T")[0] # Extract date to remove time, in the format YYYY-MM-DD
                if date not in combined_results: # Check if date is already in combined_results dictionary
                    combined_results[date] = {'TMAX': 'N/A', 'TMIN': 'N/A', 'PRCP': 'N/A'} # If date is not found, added with default 'N/A' values
                combined_results[date][datatype] = item["value"] # Add the result to the dictionary to the corresponding date and data type (e.g. add the temp for the max temp on 1/1/23)
    return combined_results # return the completed dictionary

# Parameters for API
api_key = 'kRJlFyzTWmLHsicGatbTwqyWuUOzmZoP'  # NOAA token for API
datasetid = 'GHCND' # Global Historical Climatology Network Daily      
stationid = 'GHCND:USW00024131'  # Boise Airport Station ID
datatypeids = ['TMAX', 'TMIN', 'PRCP'] # Maximum temp, minimum temp, precipitation
output_filename = 'historical_weather.csv'

# Write the header to the CSV file
with open(output_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Max Temperature (F)', 'Min Temperature (F)', 'Precipitation (mm)'])

# Loop through each year and fetch the data
current_year = datetime.now().year # Get current year
all_results = {} # Dictionary to hold yearly weather data
for year in range(2020, current_year + 1): # From 2020 through the current year, get all weather data
    yearly_data = fetch_data(year, api_key, datasetid, stationid, datatypeids) # Fetch data for specified year
    all_results.update(yearly_data) # Update dictionary with data for specified year

# Write the combined data to the CSV file
with open(output_filename, mode='a', newline='') as file: # Open output file in append mode
    writer = csv.writer(file)
    for date in sorted(all_results.keys()):
        day_data = all_results[date] # Get data for specified date
        writer.writerow([date, day_data['TMAX'], day_data['TMIN'], day_data['PRCP']]) # Write the data for the specified date to the file

# Notify user when the output file has been written
print(f"Data written to {output_filename}")
