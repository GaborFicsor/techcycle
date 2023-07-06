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

class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'acceptable_amount',
        'good_amount',
        'excellent_amount',
        'in_stock',
    )


class LaptopAdmin(admin.ModelAdmin):
    actions = [add_to_sale, remove_from_sale]
    search_fields = ('brand','model','series', 'label')
    list_filter = ('sale', 'brand', 'label')
    list_display = (
        'name',
        'label',
        'available',
        'in_stock',
        'acceptable',
        'good',
        'excellent',
        'on_sale',
        'price',
    )

            

class PhoneAdmin(admin.ModelAdmin):
    actions = [add_to_sale, remove_from_sale]
    list_filter = ('sale', 'brand')
    list_display = (
        'name',
        'available',
        'in_stock',
        'acceptable',
        'good',
        'excellent',
        'on_sale',
        'price',
    )

    @admin.action(description="Add selected items to sale")
    def add_to_sale(self, request, queryset):
        for product in queryset:
            product.sale = not product.sale
            product.save()
    

class SmartwatchAdmin(admin.ModelAdmin):
    actions = [add_to_sale, remove_from_sale]
    list_filter = ('sale', 'brand')
    list_display = (
        'name',
        'available',
        'in_stock',
        'acceptable',
        'good',
        'excellent',
        'on_sale',
        'price',
    )

class ConsoleAdmin(admin.ModelAdmin):
    actions = [add_to_sale, remove_from_sale]
    list_filter = ('sale', 'brand')
    list_display = (
        'name',
        'available',
        'in_stock',
        'acceptable',
        'good',
        'excellent',
        'on_sale',
        'price',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Smartwatch, SmartwatchAdmin)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Inventory, InventoryAdmin)
