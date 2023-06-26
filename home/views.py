import random
from django.shortcuts import render
from products.models import Laptop
from .models import FAQ


def index(request):
    """A view to return the index page"""

    laptops = list(Laptop.objects.all())
    faqs = list(FAQ.objects.all())

    laptops = random.sample(laptops, 4)

    context = {
        'laptops': laptops,
        'faqs': faqs,
    }

    return render(request, 'home/index.html', context)