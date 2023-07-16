from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    """
    A class for displaying the FAQ model's objects
    in the django default admin panel
    """
    list_display = (
        'question',
        'answer',
    )


admin.site.register(FAQ, FAQAdmin)
