import googlemaps
from datetime import datetime
import urllib.request
import json
from .weatherapi import getWeather

# Gets Directions and Weather data from APIs

class googleMapsAPI():
	# gmaps = googlemaps.Client(key='AIzaSyCxW4eIn3MlXuOLrHLiMyCNVJpuQ8lWHeA'
	
	def getCoordinates(from_location, to_location):
		endpoint = "https://maps.googleapis.com/maps/api/directions/json?"
		api_key = 'AIzaSyAoGWCOVAMqOzE7DwG8gN32fWMxQO1iXMg'
		origin = from_location.replace(" ","+")
		destination = to_location.replace(" ","+")
		nav_request = "origin=" + origin + "&destination=" + destination + "&key=" + api_key
		# request = "https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=AIzaSyAoGWCOVAMqOzE7DwG8gN32fWMxQO1iXMg&libraries=geometry"
		
		request = endpoint + nav_request
		response = urllib.request.urlopen(request).read()
		direction = json.loads(response)

		locations = []
		weather_locations = dict()
		steps = direction['routes'][0]['legs'][0]['steps']
		for i in range(1, len(steps)+1):
			locations.append(steps[i-1]['start_location'])
			# print(str(i-1) + ":" + str(steps[i-1]['start_location']))
			
			weather_locations[str(i)] = getWeather(locations[i-1])
		return [direction, locations, weather_locations]

	def reverseGeocoding(place):
		api_key = 'AIzaSyAoGWCOVAMqOzE7DwG8gN32fWMxQO1iXMg'
		request = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(place['lat']) + "," + str(place['lat']) + place + "&key=" + api_key

		location = urllib.request.urlopen(request).read()
		direction = json.loads(location)

		return location
	