from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
import os

BASE_DIR = str("/Users/muthuvel/Documents/GitHub/Distributed-Web-Application-for-travel-information/mywaypoints")
TEMPLATE_DIRS = os.path.join(BASE_DIR, 'static/')

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "index.html"

# def index (request):
#     return HttpResponse('index.html')