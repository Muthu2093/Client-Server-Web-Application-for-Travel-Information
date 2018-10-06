from django.conf.urls import url
from travelInformation import views
from django.urls import path
from . import views

## Main server url definitions
urlpatterns = [
	path('', views.HomePageView, name='home'),
    path('server/', views.getLocationMain, name='getLocationMain'),
]