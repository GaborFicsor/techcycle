from django.contrib import admin
from .models import Category, Laptop, Phone, Smartwatch, Console, Product



class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'series',
        'model'
    )

class ConditionAdmin(admin.ModelAdmin):
    list_display = (
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
    )
    

class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'series',
        'model',
        'storage_size',
        'ram',
    )
    

class SmartwatchAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'series',
        'model',
    )

class ConsoleAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'series',
        'model',
        'storage_size',
        'stock_acceptable',
        'stock_good',
        'stock_excellent'
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Smartwatch, SmartwatchAdmin)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Product, ProductAdmin)
