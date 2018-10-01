from django.shortcuts import HttpResponse
from django.views.generic import TemplateView

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.template import RequestContext
from .forms import NameForm, NameFormMain
from .googleapi import googleMapsAPI
# Main Home Page

import googlemaps
from datetime import datetime
import json

gmaps = googlemaps.Client(key='AIzaSyCxW4eIn3MlXuOLrHLiMyCNVJpuQ8lWHeA')

class f(object):
  def __init__(self):
    self.arguments = None
    self.caller = None
    self.length = 0
    self.name = ""


def HomePageView(request):
	form = NameFormMain()
	flags = "false"
	return render(request, 'index.html', {'form': form, 'flag': flags})

def getLocationMain(request):
	form = NameFormMain(request.GET)
	flags = "true"

	from_location = request.GET['from_location']
	to_location = request.GET['to_location']
	if(form.is_valid):
	    if request.method == 'GET':
	    	[directions_result, waypoints, weather_waypoints] = googleMapsAPI.getCoordinates(from_location, to_location)

	    	destination = {}
	    	origin = {}
	    	destination['query'] = str(to_location)
	    	origin['query'] = str(from_location)
	    	travelMode = "DRIVING"
	    	directions_result['request'] = {'destination' : destination, 'origin' : origin, 'travelMode' : travelMode}

	    	# print(directions_result)
	    	# print(type(directions_result['routes'][0]['legs'][0]['end_location']['lat']))
	    	# print(request)
	    	# print("location is ", directions_result['routes'][0]['legs'][0]['steps'][0]['start_location'])
	    	# text = str("WTF \
	    			# WTF")

	    	# print(weather_waypoints)
	    	# print("here\n")
	    	# print("here\n")
	    	# print("here\n")
	    	# print("here\n")
	    	# print("here\n")
	    	# print("here\n")
	    	# print("here\n")
	    	# print("here\n")
	    	# print("here\n")
	    	# print(directions_result)
	    	# print(weather_waypoints)

	    	return render(request, "index.html", 
	    		{'directions_result' : json.dumps(directions_result),
	    		'from_location' : from_location, 
	    		'to_location': to_location,
	    		# 'waypoints' : waypoints[0],
	    		# 'text' : text,
	    		'weather_waypoints' : json.dumps(weather_waypoints),
	    		'flag': flags})
	else:
		form = NameFormMain()

	return HttpResponse("Location provided in InValid.. Please Check again !!! ")

# class AboutPageView(TemplateView):
#     template_name = "map.html"

# def getLocation(request):
#     if request.method == 'GET':
#         form = NameForm(request.GET)
#         if form.is_valid():
#             return HttpResponse(form['your_name'])
#     else:
#         form = NameForm()
#     return HttpResponse("thanks")

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

# def index (request):
#     return HttpResponse("Welcome to the page")