from urllib.request import urlopen
import json
import datetime

weather_key = "601618d42787d41d986a7645681251a0"
# URL = "http://api.openweathermap.org/data/2.5/weather?q=" + str("new+york") + "&APPID=" + weather_key
# response = json.loads(urlopen(URL).read().decode('utf-8'))
# weather_key = "601618d42787d41d986a7645681251a0"

def getWeather(dictionary):
	new_response = dict()
	lat = dictionary['lat']
	lon = dictionary['lng']
	# url => http://api.openweathermap.org/data/2.5/forecast/city?id=:id&APPID=:key
	# URL = "http://api.openweathermap.org/data/2.5/weather?q=" + str(location) + "&APPID=" + weather_key
	URL = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon)  + "&APPID=" + weather_key
	response = json.loads(urlopen(URL).read().decode('utf-8'))
	print(dictionary)


	# print("here\n")
	# print("here\n")
	# print("here\n")
	# print(response)

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
		datetime.datetime.utcfromtimestamp(int(new_response['sunrise'])).strftime('%Y-%m-%dT%H:%M:%SZ')
		new_response['sunrise'] = str(new_response['sunrise'])
	except:
		new_response['sunrise'] = "Not Defined by API"

	try:
		new_response['sunset'] = str(response['sys']['sunset'])
		datetime.datetime.utcfromtimestamp(int(new_response['sunset'])).strftime('%Y-%m-%dT%H:%M:%SZ')
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

	# const text =    `<div> City: ${marker_weather.name} </div>
 #                          <div> High: ${(marker_weather.main.temp_max-273.15).toFixed(2)} C or  ${(((marker_weather.main.temp_max-273.15)*1.8)+32).toFixed(2)} F </div>
 #                          <div> Low: ${(marker_weather.main.temp_min-273.15).toFixed(2)}  C or ${(((marker_weather.main.temp_min-273.15)*1.8)+32).toFixed(2)} F </div>
 #                    <div> Sunrise ${date_rise.getHours()}:${("0"+date_rise.getMinutes()).substr(-2)}; Sunset: ${date_set.getHours()}:${("0"+date_set.getMinutes()).substr(-2)} </div>
 #                          <div> Clouds: ${marker_weather.weather[0].description} </div>
 #                          <div> Wind:  Speed-${marker_weather.wind.speed}; Degree-${marker_weather.wind.deg} </div>
 #                          <div> Humidity: ${marker_weather.main.humidity} </div>`;
 #                          var date_rise = new Date(marker_weather.sys.sunrise*1000);
 #          					var date_set = new Date(marker_weather.sys.sunset*1000);
	# # print(response)

	return new_response

	
	
	
	