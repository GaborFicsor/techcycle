from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # url for the home view
    path('', views.index, name='home'),
    path('policy', views.policy, name='policy'),
    path('conditions', views.conditions, name='conditions'),
    path('inspections', views.inspections, name='inspections'),
    path('sustainability', views.sustainability, name='sustainability'),
]
