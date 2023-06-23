from django.shortcuts import render
from .models import Laptop


def laptops(request):
    """A view to show all laptops"""

    laptops = Laptop.objects.all()

    context = {
        'laptops': laptops
    }

    return render(request, 'laptops/laptops.html', context)