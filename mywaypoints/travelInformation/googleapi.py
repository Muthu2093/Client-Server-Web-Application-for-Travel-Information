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
		origin = from_location
		destination = to_location
		nav_request = "&origin=" + origin + "&destination=" + destination + "&key=" + api_key
		request = "https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=AIzaSyAoGWCOVAMqOzE7DwG8gN32fWMxQO1iXMg&libraries=geometry"
		response = urllib.request.urlopen(request).read()
		direction = json.loads(response)

		return direction
	# from_coordinates = gmaps.reverse_geocode((40.714224, -73.961452))
		# from_coordinates = gmaps.geocode(from_location)
		# to_coordinates = gmaps.geocode(to_location)
		# now = datetime.now()

		# directions_result = gmaps.directions(from_coordinates,
  #                                    		to_coordinates,
  #                                    		mode="transit",
  #                                    		departure_time=now)
		# return directions_result

	# def getJSON(from):
	# 	https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=AIzaSyATAK_TUFNYXoj692Mt3djzreazhlWD3Do