from django.shortcuts import HttpResponse
from django.views.generic import TemplateView

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.template import RequestContext
from .forms import NameForm, NameFormMain


# BASE_DIR = str("/Users/muthuvel/Documents/GitHub/Distributed-Web-Application-for-travel-information/mywaypoints")
# TEMPLATE_DIRS = os.path.join(BASE_DIR, 'static/')

# Main Home Page

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "map.html"

# def getLocation(request):
#     if request.method == 'GET':
#         form = NameForm(request.GET)
#         if form.is_valid():
#             return HttpResponse(form['your_name'])
#     else:
#         form = NameForm()
#     return HttpResponse("thanks")

def getLocationMain(request):
    if request.method == 'GET':
        form = NameFormMain(request.GET)
        if form.is_valid():
            return HttpResponse(form)
    else:
        form = NameFormMain()
    return HttpResponse("thanks")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index (request):
    return HttpResponse("Welcome to the page")