from django.contrib import admin
from .models import Category, Laptop, Phone, Smartwatch, Console, Product, Inventory

@admin.action(description="Add selected items to sale")
def add_to_sale(self, request, queryset):
    queryset.update(sale=True)

@admin.action(description="Remove selected items from sale")
def remove_from_sale(self, request, queryset):
    queryset.update(sale=False)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class InventoryAdminInline(admin.TabularInline):
    """Inventory inline fields to display the inventory for the products"""
    model = Inventory
    readonly_fields = ('condition', 'price', 'sale_price')

class LaptopAdmin(admin.ModelAdmin):
    """Laptop admin"""
    inlines = (InventoryAdminInline,)
    actions = [add_to_sale, remove_from_sale]
    search_fields = ('brand','model','series', 'label')
    list_filter = ('sale', 'brand', 'label')
    list_display = (
        'name',
        'label',
        'price',
        'available',
        'sale',
        'in_stock',
    )

            

class PhoneAdmin(admin.ModelAdmin):
    """Phone admin"""
    inlines = (InventoryAdminInline,)
    actions = [add_to_sale, remove_from_sale]
    search_fields = ('brand','model','series')
    list_filter = ('sale', 'brand')
    list_display = (
        'name',
        'price',
        'available',
        'sale',
        'in_stock',
    )
    

class SmartwatchAdmin(admin.ModelAdmin):
    """Smartwatch admin"""
    inlines = (InventoryAdminInline,)
    actions = [add_to_sale, remove_from_sale]
    search_fields = ('brand','model','series')
    list_filter = ('sale', 'brand')
    list_display = (
        'name',
        'price',
        'available',
        'sale',
        'in_stock',
    )


class ConsoleAdmin(admin.ModelAdmin):
    """Console admin"""
    inlines = (InventoryAdminInline,)
    actions = [add_to_sale, remove_from_sale]
    search_fields = ('brand','model','series')
    list_filter = ('sale', 'brand')
    list_display = (
        'name',
        'price',
        'available',
        'sale',
        'in_stock',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Smartwatch, SmartwatchAdmin)
admin.site.register(Console, ConsoleAdmin)
