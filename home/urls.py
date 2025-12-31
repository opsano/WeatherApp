from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_page, name='search'),
    path('weather/', views.weather, name='weather'),

    path('search/api/autocomplete/', views.searchAutoComplete, name='autocomplete'), # returns an api json response
]