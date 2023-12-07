
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

## General Reflection
### Aaron
My biggest contribution here was taking the time to understand the Python syntax being used here. This was important in my overall contribution to the project, which focused on the website material. If I didn't understand the basics in this process, I would not have been able to write about it. Additionally, I made sure to give my input in group conversations and independently study the libraries/technologies that were used.

A big challenge was finding ways to make myself useful in this aspect of the project. This is definitely a new area for me, and it required a lot of effort on my part to get up to speed. I felt like I was successful in this regard, and was able to gain some confidence in how the overall project operates. I followed the lead of my teammates, and made sure to make myself available if any assistance was needed from me.

### Chiara
My contributions focused primarily around creating APIs to obtain the historical and forecasted weather data. I created two files, API.py, which contains the historical data, and ForecastedAPI.py, which contains the seven day weather forecast. API.py was the first and hence the more challenging of the two. I have never worked with APIs before, so understanding the parameters and how to create the endpoints was challenging. NCEI has an API webpage that helps users through the process, and this seems like a pretty common use of APIs so I was able to find a lot of information on how to do this. Getting the API to work and parsing through to get the data in the desired format was the most difficult part of this task, but once API.py was working, I was able to reuse a lot of the same concepts for ForecastAPI.py. The forecast information came from NWS instead of NCEI, and I found the NWS site much easier to navigate. They have a lot of documentation on the different endpoints, so once I figured out the correct location information (NCEI uses 'station ids', while NWS uses Forecast Office and gridpoint information), I was able to look at the JSON files to figure out which one provided the necessary information.

One of the biggest challenges was understanding the information and format needed to train the machine learning model. When I initially created the ForecastAPI.py file, I used daily summary information, which includes max and min temperature, but only includes whether or not precipitation is expected, but does not indicate amount. I had to create a second endpoint that looked at the hourly forecast to obtain the total expected precipitation in mm. Another hurdle was obtaining the Ridge to Rivers trail closure information. This information is not stored in an easily accessible format, and Facebook (to my knowledge) does not provide any easy way to webscrape. I had to manually look through two years of data and record which trails were closed. This process included a lot of guessing, and the reports are in paragraph format and often do not explicitly state trail closures. We initially trained the model on one year of data, but it was only accurate to 65%. We collected another year of data in hopes of increasing this percentage, but ultimately agreed that we could tolerate a low level of accuracy since the purpose of this project is to learn.

### David
My primary contributions focused on the creation and training of the model. I primarily worked on the Jupyter Notebook, ModelAPI.py, and testAPI.py. A significant challenge was training the model, as we couldn't begin without data. Fortunately, Chiara successfully set up the API and gathered all the necessary data for training. Initially, our model achieved 98% accuracy using the complete dataset from the API.

I developed a function to assign target values to the model based on precipitation and temperature ranges. However, this approach was flawed. We had anticipated obtaining these threshold values directly, but it was impractical as Chiara had to manually scrape data from Facebook and input trail closures. Instead of predicting a single column, our model had to handle a multi-label dataset, which reduced our accuracy to 60%. After hyperparameter tuning and creating a data pipeline, we managed to increase the accuracy to 64%. With Chiara's additional data collection efforts, we ultimately achieved a 68% accuracy.

Another major challenge was saving the model and integrating an API that communicated with our website. After some research browsing examples, I successfully got the API running. I also created a testAPI.py file, which served to verify its functionality and demonstrate to my teammates how to interact with the API specifically, how to request and receive data for displaying trail information.

### Drew
My main contribution to the project was the language website. I got the website running, and gave the team instructions on how to get the Node server running as well 
as how to see the website on their localhost. Next, I transferred over Aaron's content onto the website. After that, it was a matter of creating a UI for the API's that our project consisted of. I worked mainly with Chiara's ForecastAPI.py file and David's ModelAPI.py file. My initial idea was to grab the 7 day forecast, 
display it in a dropdown selectable element, and then choose one of those values to send to David's API. This ended up being the route we pursued. The main issue 
I ran into was running the python scripts within Node. Node did not like this. Further, I had to create a pythonExecutor file, which uses a shell within it to execute the python code. This allowed the scripts to be able to run, and the API's to start giving some output. The next hurdle was then having Chiara and David's API's talk 
to each other correctly. This was not easy, as there were many issues such as CSV formatting and CORS problems. Once this was solved, the API's could finally work
together and David's API started outputting the values we needed to complete our analysis (which ended up being an array of 0 and 1's). With this data, we could display the trails fit for use, on a particular day! From there, it was just a matter of morping the trails into a pretty table, which wasn't too bad. 

## Sources
Chiara Altobelli. Conversation with David Gordon, Ridge to Rivers Division Manager. Phone Call, 2023. October 24,
2023.

Ridge to Rivers. Wet Weather and Winter Trail Use. https://www.ridgetorivers.org/etiquette/
wet-weather-and-winter-trail-use/, Accessed: 2023.

How to Build an API with python FLask. \
https://www.moesif.com/blog/technical/api-development/Building-RESTful-API-with-Flask/

