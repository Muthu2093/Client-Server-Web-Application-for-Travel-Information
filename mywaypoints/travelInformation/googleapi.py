import googlemaps
from datetime import datetime
import urllib.request
import json

# Authenticate key

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

		return direction
	