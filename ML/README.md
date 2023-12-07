
# Programming Language Project

* Author: Team Flying Circus
* Members: Aaron Goin, Chiara Altobelli, David Arteaga, Drew Rizk
* Class: CS354 Section #002
* Semester: Fall 2023


## Project Description
### Background
Ridge to Rivers is a dedicated organization committed to the preservation and maintenance of the trail systems in the Boise foothills. The organization’s website offers several valuable features, including interactive and downloadable maps, detailed area descriptions, information on trail etiquette, as well as guidance on wet weather and winter trail usage (Ridge to Rivers. Wet Weather and Winter Trail Use).

Each day, a trail report is generated to report on trail accessibility. To generate the daily report, the Ridge to Rivers team conducts daily inspections of each trail, evaluating its current condition and factoring in the daily NOAA weather forecast. They assess various factors such as soil moisture and temperature fluctuations to predict which trails may become muddy and have limited accessibility during the day. The team utilizes this data to compile a comprehensive daily report and updates the interactive trail map to provide trail users with real-time information for safe and enjoyable outdoor experiences (Altobelli, 2023).

### Project Details
This project focuses on creating an interactive user interface for the Wet Weather and Winter Trail Usage section of the Ridge to Rivers website. A machine learning model was trained on historical weather and trail closure data, and then fed a seven day forecast to predict upcoming trail conditions. A user interface allows a user to select a particular day and see which trails are expected to be open based on the weather conditions.

### Weather APIs
Historical weather information for the Boise Airport Station was obtained from NCEI (National Centers for Environmental Information). Information includes the date, the maximum temperature (F), the minimum temperature (F), and the total precipitation (mm). This information was exported to a csv called historical_weather.csv. Once the weather information was obtained, trail closure information was gathered from the Ridge to Rivers Facebook webpage, where they post daily Trail Conditions Reports. Two years of data was captured, from November 2021 through November 2023.

A seven day weather forecast for the Boise Airport location was obtained from NWS (National Weather Service). The information includes the date, forecasted maximum and minimum temperatures (F), and forecasted precipitation (mm). The historical weather and trail closure information was fed to a machine learning model, which was trained to predict trail conditions for the forecasted period based on the historical data.

### Machine Learning Model
The historical weather and trail closure data was used to train a machine learning model. The model creates an API, which is then utilized in the user interface.

### User Interface
The user interface was created based on the machine learning model, and allows users to select a date in the forecasted range to see what trail conditions will be like. Trails expected to be open during the selected date are displayed so the user knows which trails are expected to be accessible based on the current conditions.

## Project semester and year

Fall Semester, 2023

## Running the program
### API.py
python API. py

### ForecastAPI.py
python ForecastAPI.py

### ModelAPI.py

$ python ModelAPI.py

provides localhost url for requests
### testAPI.py
$ python testAPI.py \
ModelAPI.py should be running before running testAPI.py \
requests a prediction from the the ModelAPI.py file.

## Sources
Chiara Altobelli. Conversation with David Gordon, Ridge to Rivers Division Manager. Phone Call, 2023. October 24,
2023.

Ridge to Rivers. Wet Weather and Winter Trail Use. https://www.ridgetorivers.org/etiquette/
wet-weather-and-winter-trail-use/, Accessed: 2023.

How to Build an API with python FLask. \
https://www.moesif.com/blog/technical/api-development/Building-RESTful-API-with-Flask/

