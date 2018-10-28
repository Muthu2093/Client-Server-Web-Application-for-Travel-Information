from urllib.request import urlopen
import json
import datetime

## Get weather information

weather_key = "601618d42787d41d986a7645681251a0"
# URL = "http://api.openweathermap.org/data/2.5/weather?q=" + str("new+york") + "&APPID=" + weather_key
# response = json.loads(urlopen(URL).read().decode('utf-8'))
# weather_key = "API_KEY"

def getWeather(dictionary):
	new_response = dict()
	lat = dictionary['lat']
	lon = dictionary['lng']
	URL = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon)  + "&APPID=" + weather_key
	response = json.loads(urlopen(URL).read().decode('utf-8'))

	## try catch is used to catch invalid data
	try:
		new_response['name'] = str(response['name'])
	except:
		new_response['name'] = "Not Defined by API"

	try:
		new_response['temp_max_c'] = str(round(response['main']['temp_max']-273.15,2))
	except:
		new_response['temp_max_c'] = "Not Defined by API"

	try:
		new_response['temp_max_f'] = str(round(((response['main']['temp_max']-273.15)*1.8)+32,2))
	except:
		new_response['temp_max_f'] = "Not Defined by API"

	try:
		new_response['temp_min_c'] = str(round(response['main']['temp_min']-273.15,2))
	except:
		new_response['temp_min_c'] = "Not Defined by API"

	try:
		new_response['temp_min_f'] = str(round(((response['main']['temp_min']-273.15)*1.8)+32,2))
	except:
		new_response['temp_min_f'] = "Not Defined by API"


	try:
		new_response['sunrise'] = str(response['sys']['sunrise'])
		new_response['sunrise'] = datetime.datetime.utcfromtimestamp(int(new_response['sunrise'])).strftime('%H:%M')
		new_response['sunrise'] = str(new_response['sunrise'])
	except:
		new_response['sunrise'] = "Not Defined by API"

	try:
		new_response['sunset'] = str(response['sys']['sunset'])
		new_response['sunset'] = datetime.datetime.utcfromtimestamp(int(new_response['sunset'])).strftime('%H:%M')
		new_response['sunset'] = str(new_response['sunset'])
	except:
		new_response['sunset'] = "Not Defined by API"

	try:
		new_response['clouds'] = str(response['weather'][0]['description'])
	except:
		new_response['clouds'] = "Not Defined by API"

	try:
		new_response['wind_speed'] = str(response['wind']['speed'])
	except:
		new_response['wind_speed'] = "Not Defined by API"

	try:
		new_response['wind_deg'] = str(response['wind']['deg'])
	except:
		new_response['wind_deg'] = "Not Defined by API"

	try:
		new_response['humidity'] = str(response['main']['humidity'])
	except:
		new_response['humidity'] = "Not Defined by API"


	return new_response

	
	
	
	