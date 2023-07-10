from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Laptop, Phone, Smartwatch, Console, Category, Product, Inventory
from django.db.models import Sum
from .forms import ProductForm


def all_products(request):

    query = None
    sort = None
    direction = None
    categories = Category.objects.values_list('friendly_name', flat=True).distinct()

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
    
    context = {
        'laptops': laptops,
        'phones': phones,
        'smartwatches': smartwatches,
        'consoles': consoles,
        'search_term': query,
        'categories': categories,
    }

    return render(request, 'products/products.html', context)

def laptops(request):
    """A view to show all laptops"""

    sort = None
    direction = None
    laptops = Laptop.objects.all()
    brands = Laptop.objects.values_list('brand', flat=True).distinct()
    inventory = Inventory.objects.all()

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
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            laptops = laptops.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'laptops': laptops,
        'current_sorting': current_sorting,
        'brands': brands,
        'inventory': inventory,
    }

    return render(request, 'laptops/laptops.html', context)

def laptop_detail(request, laptop_id):
    """A view to show an individual detailed page for laptops"""

    laptop = get_object_or_404(Laptop, pk=laptop_id)

    context = {
        'laptop': laptop,
    }

    return render(request, 'laptops/laptop_detail.html', context)

def phones(request):
    """A view to show all phones"""

    sort = None
    direction = None
    phones = Phone.objects.all()
    brands = Phone.objects.values_list('brand', flat=True).distinct()


    if request.GET:
        if 'brand' in request.GET:
            brand = request.GET['brand']
            phones = Phone.objects.filter(brand=brand)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            phones = phones.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'
    context = {
        'phones': phones,
        'current_sorting': current_sorting,
        'brands': brands,

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

    sort = None
    direction = None
    smartwatches = Smartwatch.objects.all()
    brands = Smartwatch.objects.values_list('brand', flat=True).distinct()

    if request.GET:
        if 'brand' in request.GET:
            brand = request.GET['brand']
            smartwatches = Smartwatch.objects.filter(brand=brand)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            smartwatches = smartwatches.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'
    context = {
        'smartwatches': smartwatches,
        'current_sorting': current_sorting,
        'brands': brands,
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

    sort = None
    direction = None
    consoles = Console.objects.all()
    brands = Console.objects.values_list('brand', flat=True).distinct()

    if request.GET:
        if 'series' in request.GET:
            series = request.GET['series']
            consoles = Console.objects.filter(series=series)
        if 'brand' in request.GET:
            brand = request.GET['brand']
            consoles = Console.objects.filter(brand=brand)
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            consoles = consoles.order_by(sortkey)


    current_sorting = f'{sort}_{direction}'
    context = {
        'consoles': consoles,
        'current_sorting': current_sorting,
        'brands': brands,
    }

    return render(request, 'consoles/consoles.html', context)

def console_detail(request, console_id):
    """A view to show an individual detailed page for consoles"""

    console = get_object_or_404(Console, pk=console_id)

    context = {
        'console': console
    }

    return render(request, 'consoles/console_detail.html', context)

def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messasges.success(request, 'Successfully updated product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
