from django.contrib import admin
from .models import Category, Laptop, Phone, Smartwatch, Console, Product, Inventory



class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'condition',
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
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Smartwatch, SmartwatchAdmin)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Inventory, InventoryAdmin)
