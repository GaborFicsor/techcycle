from django.urls import path
from . import views

urlpatterns = [
    # url for the profile and order_history views
    path(
        '',
        views.profile,
        name='profile'
        ),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
        ),
]
