from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Laptop, Phone, Smartwatch, Console, Category, Product


def all_products(request):

    query = None
    sort = None
    direction = None

    laptops = Laptop.objects.all()
    phones = Phone.objects.all()
    smartwatches = Smartwatch.objects.all()
    consoles = Console.objects.all()

    if request.GET:

        if 'sale' in request.GET:
            sale = request.GET['sale']
            laptops = Laptop.objects.filter(sale=True)
            phones = Phone.objects.filter(sale=True)
            smartwatches = Smartwatch.objects.filter(sale=True)
            consoles = Console.objects.filter(sale=True)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(brand__icontains=query) | Q(model__icontains=query) | Q(series__icontains=query) | Q(color__icontains=query)
            laptops = laptops.filter(Q(category__name__icontains=query) | queries)
            phones = phones.filter(Q(category__name__icontains=query) | queries)
            smartwatches = smartwatches.filter(Q(category__name__icontains=query) | queries)
            consoles = consoles.filter(Q(category__name__icontains=query) | queries)
    
    current_sorting = f'{sort}_{direction}'
    context = {
        'laptops': laptops,
        'phones': phones,
        'smartwatches': smartwatches,
        'consoles': consoles,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def laptops(request):
    """A view to show all laptops"""

    laptops = Laptop.objects.all()

    if request.GET:
        if 'brand' in request.GET:
            brand = request.GET['brand']
            laptops = Laptop.objects.filter(brand=brand)

        if 'label' in request.GET:
            label = request.GET['label']
            laptops = Laptop.objects.filter(label=label)
    
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
        if sortkey == 'price':
            laptops = laptops.order_by('price')

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

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
        if sortkey == 'price':
            phones = phones.order_by('price')

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

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
        if sortkey == 'price':
            smartwatches = smartwatches.order_by('price')

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

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
        if sortkey == 'price':
            consoles = consoles.order_by('price')

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