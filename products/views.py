from django.shortcuts import render, get_object_or_404
from .models import Laptop, Phone


def laptops(request):
    """A view to show all laptops"""

    laptops = Laptop.objects.all()

    context = {
        'laptops': laptops
    }

    return render(request, 'laptops/laptops.html', context)

def laptop_detail(request, laptop_id):
    """A view to show an individual detailed page for laptops"""

    laptop = get_object_or_404(Laptop, pk=laptop_id)

    context = {
        'laptop': laptop
    }

    return render(request, 'laptops/laptop_detail.html', context)

def phones(request):
    """A view to show all phones"""

    phones = Phone.objects.all()

    context = {
        'phones': phones
    }

    return render(request, 'phones/phones.html', context)

def phone_detail(request, phone_id):
    """A view to show an individual detailed page for phones"""

    phone = get_object_or_404(Phone, pk=phone_id)

    context = {
        'phone': phone
    }

    return render(request, 'phones/phone_detail.html', context)