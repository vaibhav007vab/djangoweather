
# this is my views.py file
from django.urls import path
from . import views 

urlpatterns = [
 path('', views.home, name="home"),
 ##path('add_city.html', views.add_city, name="add_city"),
 #path('add_country.html', views.add_country, name="add_country"),
 path('about.html', views.about, name="about"),

]
