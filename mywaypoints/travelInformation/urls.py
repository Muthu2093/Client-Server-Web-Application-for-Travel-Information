from django.conf.urls import url
from travelInformation import views
from django.urls import path
from . import views

urlpatterns = [
    # url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    # url(r'^about/$',s views.AboutPageView.as_view(), name='about'),

    path('', views.HomePageView.as_view(), name='home'),
    path('about', views.AboutPageView.as_view(), name='about'),
    # ex: /polls/5/
    # path('your-name/', views.getLocation, name='getLocation'),
    path('weather/', views.getLocationMain, name='getLocationMain'),
    # path('<slug:from_loc>/<slug:to_loc>/', views.getLocation, name='getLocation'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]