import googlemaps
from datetime import datetime

# Authenticate key
gmaps = googlemaps.Client(key='AIzaSyCxW4eIn3MlXuOLrHLiMyCNVJpuQ8lWHeA')

class googleMapsAPI():
	
	def getCoordinates(from_location, to_location):
	# from_coordinates = gmaps.reverse_geocode((40.714224, -73.961452))
		from_coordinates = gmaps.geocode(from_location)
		to_coordinates = gmaps.geocode(to_location)
		now = datetime.now()

		directions_result = gmaps.directions(from_coordinates,
                                     		to_coordinates,
                                     		mode="transit",
                                     		departure_time=now)
		return directions_result

	def getJSON(from)
	https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=AIzaSyATAK_TUFNYXoj692Mt3djzreazhlWD3Do