from django.urls import path
from . import views

urlpatterns = [
    path('laptops', views.laptops, name='laptops'),
    path('laptops/<laptop_id>', views.laptop_detail, name='laptop_detail'),
    path('phones', views.phones, name='phones'),
    path('phones/<phone_id>', views.phone_detail, name='phone_detail'),
]
