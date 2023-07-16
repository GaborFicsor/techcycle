import random
from django.shortcuts import render
from products.models import Laptop
from .models import FAQ


def index(request):
    """
    A view to render the index page, the FAQs and also return
    a list of randomly selected objects from the Laptop model
    """

    laptops = list(Laptop.objects.filter(label='Gaming Laptop'))
    faqs = list(FAQ.objects.all())

    laptops = random.sample(laptops, 4)

    context = {
        'laptops': laptops,
        'faqs': faqs,
    }

    return render(request, 'home/index.html', context)
