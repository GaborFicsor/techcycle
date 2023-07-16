from django.urls import path
from . import views


urlpatterns = [
    # urls for the view, add_to_bag and remove_from_bag views
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove/<item_id>', views.remove_from_bag, name='remove_from_bag')
]
