# Client-Server-Web-Application-for-Travel-Information
This application is developed in Django Framework and it provides an improved GoogleMaps Directions Response by providing travel Information along the route when you input a start and end location. 

The amazing part is that you do not need to query Google or Weather API more than once since the query information is cached in a MySQL database !

## A Simple Work-Flow of the Application
![alt text](https://github.com/Muthu2093/Client-Server-Web-Application-for-Travel-Information/blob/master/screenshots/workflow.png)

## Home Page
![alt text](https://github.com/Muthu2093/Client-Server-Web-Application-for-Travel-Information/blob/master/screenshots/hompage.png)

## Input your Start and End Location
![alt text](https://github.com/Muthu2093/Client-Server-Web-Application-for-Travel-Information/blob/master/screenshots/Clientpage.png)

## Get Weather and Travel Information
![alt text](https://github.com/Muthu2093/Client-Server-Web-Application-for-Travel-Information/blob/master/screenshots/Responsereceived.png)

## Getting Started

The repository could be downloaded and the web-application can be hosted in a local server  

### Prerequisites

The project requires the following modules to work 
```
Python 3
```

```
Django 2.1.0
```

```
MySQL
```

The API calls to Google MAPS and OpenWeather requires you to get developer account for both. My suggesstion is to use a virutal environment or a conda environement to install all dependencies

### Installing

Python
```
https://www.python.org/downloads/
```

Follow the link below to install Django libraries
```
https://www.djangoproject.com/download/
```

To set up a mysql database follow the instructions in the link below
```
https://www.mysql.com/downloads/
```

Follow Links below to get Developer Accounts from Google and OpenWeather and store the API keys
```
https://developers.google.com/maps/documentation/directions/intro
```
```
https://openweathermap.org/api
```

## Host the application on a your Local Server

### Placing API keys

mywaypoints is a django project. It contains all the necessary files inside

Go to mywaypoints/travelInformation/googleapi.py and change the api key from XXXXX to your own key

Go to mywaypoints/travelInformation/weatherapi.py and change the api key from XXXXX to your own key

Go to mywaypoints/travelInformation/templates/index.html put your Google API_KEY in line 150

Go to mywaypoints/travelInformation/views.py and place your Google API_KEY in Line 21

###  Start server

Goto mywaypoint/ in terminal and run the following command

``` python
python manage.py runserver

```

Go to http://127.0.0.1:8000 and Voila ! Enjoy the application


## Authors

* **Muthuvel Palanisamy** - *Initial work* - [muthu2093](https://github.com/muthu2093)

See also the list of [contributors](https://github.com/Muthu2093/Client-Server-Web-Application-for-Travel-Information/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## References

[1] https://docs.djangoproject.com/en/2.1/
