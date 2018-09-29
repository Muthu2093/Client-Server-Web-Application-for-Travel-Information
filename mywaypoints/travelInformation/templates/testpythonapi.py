import urllib.request
import json
endpoint = 'https://googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyAoGWCOVAMqOzE7DwG8gN32fWMxQO1iXMg'
origin = "Chicago"
destination = "Miami"
nav_request = "&origin=" + origin + "&destination=" + destination + "&key=" + api_key
request = "https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=AIzaSyAoGWCOVAMqOzE7DwG8gN32fWMxQO1iXMg"

response = urllib.request.urlopen(request).read()
direction = json.loads(response)

# print(direction)