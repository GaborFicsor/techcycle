from django.urls import path
from . import views

urlpatterns = [
    # All products url
    path(
        '',
        views.all_products,
        name='products'
        ),

    # Laptop urls
    path(
        'laptops/',
        views.laptops,
        name='laptops'
        ),
    path(
        'laptops/<int:laptop_id>/',
        views.laptop_detail,
        name='laptop_detail'
        ),
    path(
        'add/laptop/',
        views.add_laptop,
        name='add_laptop'
        ),
    path(
        'edit/laptop/<int:product_id>/',
        views.edit_laptop,
        name='edit_laptop'
        ),
    path(
        'edit/laptop/<int:product_id>/inventory/',
        views.edit_laptop_inventory,
        name='edit_laptop_inventory'
        ),

    # Phone urls
    path(
        'phones/',
        views.phones,
        name='phones'
    ),
    path(
        'phones/<int:phone_id>/',
        views.phone_detail,
        name='phone_detail'
        ),
    path(
        'add/phone/',
        views.add_phone,
        name='add_phone'
        ),
    path(
        'edit/phone/<int:product_id>/',
        views.edit_phone,
        name='edit_phone'
        ),
    path(
        'edit/phone/<int:product_id>/inventory/',
        views.edit_phone_inventory,
        name='edit_phone_inventory'
        ),

    # Smartwatch urls
    path(
        'smartwatches/',
        views.smartwatches,
        name='smartwatches'
        ),
    path(
        'smartwatches/<int:smartwatch_id>/',
        views.smartwatch_detail,
        name='smartwatch_detail'
        ),
    path(
        'add/smartwatch/',
        views.add_smartwatch,
        name='add_smartwatch'
        ),
    path(
        'edit/smartwatch/<int:product_id>/',
        views.edit_smartwatch,
        name='edit_smartwatch'
        ),
    path(
        'edit/smartwatch/<int:product_id>/inventory/',
        views.edit_smartwatch_inventory,
        name='edit_smartwatch_inventory'
        ),

    # Console urls
    path(
        'consoles/',
        views.consoles,
        name='consoles'
        ),
    path(
        'consoles/<int:console_id>/',
        views.console_detail,
        name='console_detail'
        ),
    path(
        'add/console/',
        views.add_console,
        name='add_console'
        ),
    path(
        'edit/console/<int:product_id>/',
        views.edit_console,
        name='edit_console'
        ),
    path(
        'edit/console/<int:product_id>/inventory/',
        views.edit_console_inventory,
        name='edit_console_inventory'
        ),

    # Url for deleting objects
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'
        ),
]
