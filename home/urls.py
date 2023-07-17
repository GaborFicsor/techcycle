from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # url for the home view
    path('', views.index, name='home'),
]
