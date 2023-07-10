from django.urls import path
from . import views

urlpatterns = [
    path('laptops/', views.laptops, name='laptops'),
    path('laptops/<int:laptop_id>/', views.laptop_detail, name='laptop_detail'),
    path('phones/', views.phones, name='phones'),
    path('phones/<int:phone_id>/', views.phone_detail, name='phone_detail'),
    path('smartwatches/', views.smartwatches, name='smartwatches'),
    path('smartwatches/<int:smartwatch_id>/', views.smartwatch_detail, name='smartwatch_detail'),
    path('consoles/', views.consoles, name='consoles'),
    path('consoles/<int:console_id>/', views.console_detail, name='console_detail'),
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
]
