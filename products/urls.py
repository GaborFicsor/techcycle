from django.urls import path
from . import views

urlpatterns = [
    path('', views.laptops, name='laptops'),
    path('<laptop_id>', views.laptop_detail, name='laptop_detail'),
]
