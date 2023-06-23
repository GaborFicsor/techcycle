from django.contrib import admin
from .models import Category, Laptop, Phone, Smartwatch, Console




class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class LaptopAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'series',
        'model',
        'cpu_brand',
        'cpu_name',
        'storage_size',
        'ram',
        'sale',
        'price',
    )
    

class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'series',
        'model',
        'storage_size',
        'ram',
        'sale',
        'price',
    )
    

class SmartwatchAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'series',
        'model',
        'sale',
        'price',
    )
    

class ConsoleAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'series',
        'model',
        'storage_size',
        'sale',
        'price',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Smartwatch, SmartwatchAdmin)
admin.site.register(Console, ConsoleAdmin)