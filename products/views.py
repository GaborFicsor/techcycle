from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Laptop, Phone, Smartwatch, Console, Category


# def search(request):
#     categories = Category.objects.all()
#     laptops = Laptop.objects.all()
#     phones = Phone.objects.all()
#     smartwatches = Smartwatch.objects.all()
#     consoles = Console.objects.all()

#     products = list(laptops) + list(phones) + list (smartwatches) +list(consoles)

#     if request.GET:
#         if 'q' in request.GET:
#             query = request.GET['q']
#             if not query:
#                 messages.error(request, "You didn't enter any search criteria")
#                 return redirect(reverse('laptops'))

#             queries = Q(brand__icontains=query) | Q(model__icontains=query) | Q(series__icontains=query) | Q(color__icontains=query) 
#             laptops = laptops.filter(
#                 Q(label__icontains=query) | Q(cpu_name__icontains=query) | Q(gpu__icontains=query) | Q(os__icontains=query)
#             )
#             phones = phones.filter(queries)
#             smartwatches = smartwatches.filter(queries)
#             consoles = consoles.filter(queries)

    
#     context = {
#         'products': products,
#         'laptops': laptops,
#         'phones': phones,
#         'smartwatches': smartwatches,
#         'consoles': consoles,
#         'search_term': query,
#     }

#     return render(request, 'search/search.html', context)


def all_products(request):
    categories = Category.objects.all()
    laptops = Laptop.objects.all()
    phones = Phone.objects.all()
    smartwatches = Smartwatch.objects.all()
    consoles = Console.objects.all()

    products = list(laptops) + list(phones) + list (smartwatches) +list(consoles)

    # if request.GET:
    #     if 'q' in request.GET:
    #         query = request.GET['q']
    #         if not query:
    #             messages.error(request, "You didn't enter any search criteria")
    #             return redirect(reverse('laptops'))

    #         queries = Q(brand__icontains=query) | Q(model__icontains=query) | Q(series__icontains=query) | Q(color__icontains=query) 
    #         laptops = laptops.filter(
    #             Q(label__icontains=query) | Q(cpu_name__icontains=query) | Q(gpu__icontains=query) | Q(os__icontains=query)
    #         )
    #         phones = phones.filter(queries)
    #         smartwatches = smartwatches.filter(queries)
    #         consoles = consoles.filter(queries)

    
    context = {
        'products': products,
        'laptops': laptops,
        'phones': phones,
        'smartwatches': smartwatches,
        'consoles': consoles,
    }

    return render(request, 'products/products.html', context)

def laptops(request):
    """A view to show all laptops"""

    laptops = Laptop.objects.all()

    if request.GET:
        if 'brand' in request.GET:
            brand = request.GET['brand']
            laptops = Laptop.objects.filter(brand=brand)

    if request.GET:
        if 'label' in request.GET:
            label = request.GET['label']
            laptops = Laptop.objects.filter(label=label)

    context = {
        'laptops': laptops,
    }

    return render(request, 'laptops/laptops.html', context)

def laptop_detail(request, laptop_id):
    """A view to show an individual detailed page for laptops"""

    laptop = get_object_or_404(Laptop, pk=laptop_id)
    condition = laptop.condition

    context = {
        'laptop': laptop,
        'condition': condition

    }

    return render(request, 'laptops/laptop_detail.html', context)

def phones(request):
    """A view to show all phones"""

    phones = Phone.objects.all()

    if request.GET:
        if 'brand' in request.GET:
            brand = request.GET['brand']
            phones = Phone.objects.filter(brand=brand)

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

def smartwatches(request):
    """A view to show all smartwatches"""

    smartwatches = Smartwatch.objects.all()

    if request.GET:
        if 'brand' in request.GET:
            brand = request.GET['brand']
            smartwatches = Smartwatch.objects.filter(brand=brand)

    context = {
        'smartwatches': smartwatches
    }

    return render(request, 'smartwatches/smartwatches.html', context)

def smartwatch_detail(request, smartwatch_id):
    """A view to show an individual detailed page for smartwatch"""

    smartwatch = get_object_or_404(Smartwatch, pk=smartwatch_id)

    context = {
        'smartwatch': smartwatch
    }

    return render(request, 'smartwatches/smartwatch_detail.html', context)

def consoles(request):
    """A view to show all consoles"""

    consoles = Console.objects.all()

    if request.GET:
        if 'series' in request.GET:
            series = request.GET['series']
            consoles = Console.objects.filter(series=series)
        elif 'brand' in request.GET:
            brand = request.GET['brand']
            consoles = Console.objects.filter(brand=brand)

    context = {
        'consoles': consoles
    }

    return render(request, 'consoles/consoles.html', context)

def console_detail(request, console_id):
    """A view to show an individual detailed page for consoles"""

    console = get_object_or_404(Console, pk=console_id)

    context = {
        'console': console
    }

    return render(request, 'consoles/console_detail.html', context)