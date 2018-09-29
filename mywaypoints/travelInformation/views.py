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
	    	# print(form)
	    	# directions_result = gmaps.directions(from_location,
      #                                		to_location,
      #                                		mode="transit",
      #                                		departure_time=datetime.now())
	    	directions_result = googleMapsAPI.getCoordinates(from_location, to_location)
	    	return HttpResponse(directions_result)
	    	# print(str(from_location) + str(to_location))
	    	# directions_result= json.dumps(directions_result)
	    	# directions_result = json.loads(directions_result)
	    	# print(directions_result)
	    	# print(directions_result.type())
	    	# return render(request, 'index.html', {'directions_result' : json.dumps(directions_result)})
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