from django.urls import path
from . import views

urlpatterns = [
    path('', views.laptops, name='laptops')
]
