from django.urls import path
from . import views

app_name = 'covid'
urlpatterns = [
    path('covid19/', views.covid_chart, name='covid-chart')
    # path('population-chart/', views.population_chart, name='population-chart')
]