from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from django.db import models

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.template import RequestContext
from .forms import NameForm, NameFormMain
from .googleapi import googleMapsAPI
from .models import MyModel
from django.db.models import Q
# Main Home Page

import googlemaps
from datetime import datetime
import json

import time

gmaps = googlemaps.Client(key='AIzaSyCxW4eIn3MlXuOLrHLiMyCNVJpuQ8lWHeA')


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
	    	# MyModel.objects.all().delete()

	    	try:
	    		start = time.time()
	    		print("Cost of Database Access c1:")
		    	all_entries = MyModel.objects.all()
		    	res = all_entries.get(
		    		Q(start=str(from_location)),
	    			Q(end=str(to_location))
	    			)
		    	directions_result = json.loads(res.attrs)
		    	weather_waypoints = json.loads(res.weather)
		    	print("Database Query")

		    	end = time.time()
		    	print("Time: ", (end-start))

	    	except:

	    		start = time.time()
	    		print("Cost of API Access :")
	    		[directions_result, waypoints, weather_waypoints] = googleMapsAPI.getCoordinates(from_location, to_location)
		    	destination = {}
		    	origin = {}
		    	destination['query'] = str(to_location)
		    	origin['query'] = str(from_location)
		    	travelMode = "DRIVING"
		    	directions_result['request'] = {'destination' : destination, 'origin' : origin, 'travelMode' : travelMode}
		    	
		    	# if (directions_result['status'] != "OK"):
		    	# 	return render(request, "index.html", {'flag': 5})
		    	
		    	data_table = MyModel()
		    	data_table.start = request.GET['from_location']
		    	data_table.end = request.GET['to_location']
		    	data_table.attrs = json.dumps(directions_result)
		    	data_table.weather = json.dumps(weather_waypoints)
		    	data_table.save()
		    	print("API call")

		    	end = time.time()
		    	print("Time", (end-start))


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
