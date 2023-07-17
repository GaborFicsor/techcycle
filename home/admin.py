from django.contrib import admin
from .models import FAQ, Newsletter


class FAQAdmin(admin.ModelAdmin):
    """
    A class for displaying the FAQ model's objects
    in the django default admin panel
    """
    list_display = (
        'question',
        'answer',
    )


class NewsletterAdmin(admin.ModelAdmin):
    """
    A class for displaying the newsletter model's
    objects in the django default admin panel
    """
    list_display = (
        'email',
    )


admin.site.register(FAQ, FAQAdmin)
admin.site.register(Newsletter, NewsletterAdmin)