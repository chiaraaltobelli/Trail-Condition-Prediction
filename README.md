
# Language Website

* Author: Team Flying Circus
* Members: Aaron Goin, Chiara Altobelli, David Arteaga, Drew Rizk
* Class: CS354 Section #002
* Semester: Fall 2023


## Project Description
The purpose of this project is to explore a new programming language and showcase it's abilities by creating a website. We selected Python for this project due to its popular application in the field of machine learning.

Our project focuses on predicting trail conditions in Boise based on historical weather and trail data. This involved utilizing APIs to gather weather data, which was then used to train a machine learning model capable of forecasting trail conditions. We chose this project to highlight some of Python's most notable features: its simplicity, readability, and its extensive library support.

The layout of our website is designed to not only demonstrate our project but also provide background and educational resources beneficial to developers new to Python. Our website includes the following sections:

### History
This section discusses the history of Python, its origins, and its development in the 1980s by Guido van Rossum, whose inspiration was drawn from the ABC language. A focal point of the discussion is Python’s user-friendly syntax, which facilitates simple code writing, and its traits as a dynamically typed language. In the field of Machine Learning, there are a wide variety of libraries Python offers for various stages of the process. This section explains how these tools streamline the process of creating and training models but also provide robust methods for evaluation and optimization.

### Get Started with Python
This section highlights materials that the Python language has to offer, such as the approved docs and various tutorials that can be used to achieve different things that the language has to offer, such as scripting tutorials and automation, machine learning workflows, and website development (Python Documentation).

This section also describes how to install Python, as well as efficient ways to download and start using its many libraries. Important factors include things like needed IDEs and common interfaces that can be downloaded in order to interact with Python and the frequently used libraries.

A few general programs are also included in this section to exhibit how Python works as well as an overview of related languages while comparing them in terms of language type, scope, and bindings. This section compares Python with the following languages in this fashion: R, JavaScript, and Java. Each of these languages have enough similarities to be considered related, all while having enough differences to compare with Python’s unique aspects.

### About
This section gives a basic overview of our project and explains the main components, including the weather APIs, the machine learning component, and the user interface.

## Project semester and year

Fall Semester, 2023

## Running the program
To run the example code on non-project tabs (tabs besides projectAPI.html), just follow the instructions as stated on the site. It will also require following previous steps (installing python, etc.), and then copying/pasting code into the environment you want to run it from.

## General Reflection
### Aaron
My biggest contribution was the actual website material: going over the language history, installation instructions, relevance to the project, characteristics of Python, etc. I also made sure to strategically place the text on the website in ways that were readable. This required a lot of research on my part, and understanding of how the project tied into the Python as a whole. It was a rewarding experience, especially discovering the community itself, and seeing how prevalent this language is in our everyday lives.

The biggest struggle actually came from the project part, as I had a lot of catching up to do in terms of getting from hello world (other basic concepts) to doing machine learning in Python. That took more time than actually writing the material for the website. I'm glad I took my time to do that, as it helped me know what to write about.

### Chiara
My contributions focused mainly around the NOAA and NWS APIs for the project, but I helped Drew a bit with the 'Our Project' tab of the website. I helped create the 'Get Weather Forecast' and 'Run Model' buttons as well as the drop down to select the correct date. Drew and I worked together to understand how to get the APIs to work on the website, and some of the more challenging aspects included understanding the correct format for the forecast API, which involved adding JSON output in addition to the existing csv file, and getting the model API to run correctly. I have never worked with machine learning before, and understanding the ML Model API file and getting all of the correct tools installed took some time. I have also never worked with HTML, and I found learning the formatting and how to insert scripts fun and engaging.

### David
My primary contributions were around the machine learning aspects of our project. Additionally, I focused on improving the visual appeal of the background and table. Specifically, I added a background image and modified the table's design to ensure readability against the new background.

Being unfamiliar with JavaScript, HTML, or CSS, this was a challenge for me. I dedicated time to learning and understanding how the front end of the website operates. This included understanding how the front end interacts with the Model API to effectively display information to the user. My modifications to the front end were minimal but helped in making the Our Project section more readable and visually appealing to the user.

### Drew
My main contribution was creating the website itself. I relied on David and Chiara to get their API's working, and Aaron mainly for the website content (which 
each of them have already described/stated). Further, my task came down to learning how to use the express app to best 'express' their work. Firstly, I moved all 
of Aaron's .md content over to the website. I started with some general HTMl and CSS to get a nav bar with a few different tabs, and then transferred over the 
.md content to its respective tab (all the while I was looking over Aaron's content he wrote trying to proofread and make sure I understood it). Secondly, I had to then focus on what I viewed as the hard part of my tasking, which was bringing Chiara and David's API's to life within the application. In short, this was a pain.
Using express and vanilla javascript was somewhat new to me, which made for a lot of overhead. However, with some time and dedication (as well as some help from Chiara and the internet), we were able to get the API's integrated into the site and working with the UI. Lastly, I guess I would say I had to dabble a little more in the ML than I thought, which isn't a bad thing whatsoever. I just didn't plan for how much I'd have to look through and use Jupyter Notebook as well as the python API files. In retropsect, I should've assumed this would be the case as integrating API's requires a foundational knowledge of the API you're implementing (at least in my opinion).

## Sources
Class Materials. Accessed: 2023.\
Flask Documentation. https://www.planeks.net/what-is-flask-used-for/, Accessed: 2023.\
Matplotlib Documentation. https://matplotlib.org/, Accessed: 2023.\
Numpy Documentation. https://numpy.org/, Accessed: 2023.\
Pip Download. https://pip.pypa.io/en/stable/installation/, Accessed: 2023.\
Python Community. https://www.python.org/community/, Accessed: 2023.\
Python Discord. https://www.pythondiscord.com/, Accessed: 2023.\
Python Documentation. https://docs.python.org/3/reference/index.html, Accessed: 2023.\
Python Download. https://www.python.org/downloads/, Accessed: 2023.\
Python Download Info. https://wiki.python.org/moin/BeginnersGuide/Download, Accessed: 2023.\
Python Frameworks. https://wiki.python.org/moin/WebFrameworks/, Accessed: 2023.\
Python History Documentation. https://beapython.dev/2021/07/25/guido-van-rossum-and-the-rise-of-python/, Accessed: 2023.\
Python Machine Learning. https://realpython.com/tutorials/machine-learning/, Accessed: 2023.\
Python Scripting. https://learn.microsoft.com/en-us/windows/python/scripting, Accessed: 2023.\
Python Web Development. https://www.educative.io/blog/web-development-in-python, Accessed: 2023.\
Ridge to Rivers Categories. https://www.ridgetorivers.org/etiquette/wet-weather-and-winter-trail-use/, Accessed: 2023.\
scikit-learn Documentation. https://scikit-learn.org/stable/index.html, Accessed: 2023.\
scikit-learn ML Model. https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html, Accessed: 2023.\
Seaborn Documentation. https://seaborn.pydata.org/, Accessed: 2023.\
VS Code Download. https://code.visualstudio.com/download, Accessed: 2023.
