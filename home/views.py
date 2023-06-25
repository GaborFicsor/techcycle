import random
from django.shortcuts import render
from products.models import Laptop


def index(request):
    """A view to return the index page"""

    laptops = list(Laptop.objects.all())

    laptops = random.sample(laptops, 4)

    context = {
        'laptops': laptops
    }

    return render(request, 'home/index.html', context)