from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import (
    Laptop, Phone, Smartwatch, Console, Category, Product, Inventory
)
from django.db.models import Sum
from .forms import (
    LaptopForm, PhoneForm, SmartwatchForm, ConsoleForm, InventoryForm
)
from decimal import Decimal
from django.forms import inlineformset_factory

from django.db.models.functions import Concat
from django.db.models import Value


def all_products(request):
    """
    A view to render all products in a template.
    Products can be filtered by:
        - search term
        - Products on sale
    """
    query = None
    sort = None
    direction = None
    categories = Category.objects.values_list(
        'friendly_name', flat=True).distinct()

    products = Product.objects.all()
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

            queries = (Q(brand__icontains=query) | Q(model__icontains=query) |
                       Q(series__icontains=query) | Q(color__icontains=query))

            laptops = laptops.filter(
                Q(category__name__icontains=query) |
                Q(label__icontains=query) | queries
                )

            phones = phones.filter(
                Q(category__name__icontains=query) | queries
                )

            smartwatches = smartwatches.filter(
                Q(category__name__icontains=query) | queries
                )

            consoles = consoles.filter(
                Q(category__name__icontains=query) | queries
                )
            products = products.filter(queries)

    context = {
        'products': products,
        'laptops': laptops,
        'phones': phones,
        'smartwatches': smartwatches,
        'consoles': consoles,
        'search_term': query,
        'categories': categories,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def laptops(request):
    """
    A view to display all objects of the Laptop model.
    Sorting is available by price.
    """
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
    """
    A view to render an individual detailed page for a Laptop object.
    """
    laptop = get_object_or_404(Laptop, pk=laptop_id)

    context = {
        'laptop': laptop,
    }

    return render(request, 'laptops/laptop_detail.html', context)


def phones(request):
    """
    A view to display all objects of the Phone model.
    Sorting is available by price.
    """
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
    """
    A view to render an individual detailed page for a Phone object.
    """
    phone = get_object_or_404(Phone, pk=phone_id)

    context = {
        'phone': phone
    }

    return render(request, 'phones/phone_detail.html', context)


def smartwatches(request):
    """
    A view to display all objects of the Smartwatch model.
    Sorting is available by price.
    """
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
    """
    A view to render an individual detailed page for a Smartwatch object.
    """
    smartwatch = get_object_or_404(Smartwatch, pk=smartwatch_id)

    context = {
        'smartwatch': smartwatch
    }

    return render(request, 'smartwatches/smartwatch_detail.html', context)


def consoles(request):
    """
    A view to display all objects of the Console model.
    Sorting is available by price.
    """
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
    """
    A view to render an individual detailed page for a Console object.
    """

    console = get_object_or_404(Console, pk=console_id)

    context = {
        'console': console
    }

    return render(request, 'consoles/console_detail.html', context)


# views for creating objects
@login_required
def add_laptop(request):
    """
    A view for creating a Laptop object.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        laptop_form = LaptopForm(request.POST)
        if laptop_form.is_valid():
            product = laptop_form.save()
            messages.success(request, 'Successfully added laptop!')
            return redirect(reverse('laptop_detail', args=[product.id]))
    else:
        laptop_form = LaptopForm()

    template = 'products/add_laptop.html'
    context = {
        'laptop_form': laptop_form,
    }

    return render(request, template, context)


@login_required
def add_phone(request):
    """
    A view for creating a Phone object.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        phone_form = PhoneForm(request.POST)
        if phone_form.is_valid():
            product = phone_form.save()
            messages.success(request, 'Successfully added Phone!')
            return redirect(reverse('phone_detail', args=[product.id]))
    else:
        phone_form = PhoneForm()

    template = 'products/add_phone.html'
    context = {
        'phone_form': phone_form,
    }

    return render(request, template, context)


@login_required
def add_smartwatch(request):
    """
    A view for creating a Smartwatch object.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        smartwatch_form = SmartwatchForm(request.POST)
        if smartwatch_form.is_valid():
            product = smartwatch_form.save()
            messages.success(request, 'Successfully added Smartwatch!')
            return redirect(reverse('smartwatch_detail', args=[product.id]))
    else:
        smartwatch_form = SmartwatchForm()

    template = 'products/add_smartwatch.html'
    context = {
        'smartwatch_form': smartwatch_form,
    }

    return render(request, template, context)


@login_required
def add_console(request):
    """
    A view for creating a Console object.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        console_form = ConsoleForm(request.POST)
        if console_form.is_valid():
            product = console_form.save()
            messages.success(request, 'Successfully added Console!')
            return redirect(reverse('console_detail', args=[product.id]))
    else:
        console_form = ConsoleForm()

    template = 'products/add_console.html'
    context = {
        'console_form': console_form,
    }

    return render(request, template, context)


# views for editing objects
@login_required
def edit_laptop(request, product_id):
    """
    A view for editing an existing Laptop object.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    laptop = get_object_or_404(Laptop, pk=product_id)
    if request.method == 'POST':
        laptop_form = LaptopForm(request.POST, request.FILES, instance=laptop)
        if laptop_form.is_valid():
            laptop = laptop_form.save()  # Update the existing instance
            messages.success(request, f'Successfully updated {laptop}')
            return redirect(reverse('laptop_detail', args=[laptop.id]))

        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        laptop_form = LaptopForm(instance=laptop)
        messages.info(request, f'You are editing {laptop}')

    template = 'products/edit_laptop.html'
    context = {
        'laptop_form': laptop_form,
        'laptop': laptop
    }

    return render(request, template, context)


@login_required
def edit_phone(request, product_id):
    """
    A view for editing an existing Phone object.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    phone = get_object_or_404(Phone, pk=product_id)
    if request.method == 'POST':
        phone_form = PhoneForm(request.POST, request.FILES, instance=phone)
        if phone_form.is_valid():
            phone = phone_form.save()  # Update the existing instance
            messages.success(request, f'Successfully updated {phone}')
            return redirect(reverse('phone_detail', args=[phone.id]))

        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        phone_form = PhoneForm(instance=phone)
        messages.info(request, f'You are editing {phone}')

    template = 'products/edit_phone.html'
    context = {
        'phone_form': phone_form,
        'phone': phone
    }

    return render(request, template, context)


@login_required
def edit_smartwatch(request, product_id):
    """
    A view for editing an existing Smartwatch object.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    smartwatch = get_object_or_404(Smartwatch, pk=product_id)
    if request.method == 'POST':
        smartwatch_form = SmartwatchForm(
            request.POST,
            request.FILES,
            instance=smartwatch
            )
        if smartwatch_form.is_valid():
            smartwatch = smartwatch_form.save()
            messages.success(request, f'Successfully updated {smartwatch}')
            return redirect(reverse('smartwatch_detail', args=[smartwatch.id]))

        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
                )
    else:
        smartwatch_form = SmartwatchForm(instance=smartwatch)
        messages.info(request, f'You are editing {smartwatch}')

    template = 'products/edit_smartwatch.html'
    context = {
        'smartwatch_form': smartwatch_form,
        'smartwatch': smartwatch
    }

    return render(request, template, context)


@login_required
def edit_console(request, product_id):
    """
    A view for editing an existing Console object.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    console = get_object_or_404(Console, pk=product_id)
    if request.method == 'POST':
        console_form = ConsoleForm(
            request.POST, request.FILES, instance=console
            )
        if console_form.is_valid():
            console = console_form.save()
            messages.success(request, f'Successfully updated {console}')
            return redirect(reverse('console_detail', args=[console.id]))

        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
                )
    else:
        console_form = ConsoleForm(instance=console)
        messages.info(request, f'You are editing {console}')

    template = 'products/edit_console.html'
    context = {
        'console_form': console_form,
        'console': console
    }

    return render(request, template, context)


# views for editing object inventories
@login_required
def edit_laptop_inventory(request, product_id):
    """
    A view for editing an existing Laptop object's inventory objects.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    laptop = get_object_or_404(Laptop, pk=product_id)
    InventoryFormSet = inlineformset_factory(
        Product,
        Inventory,
        form=InventoryForm,
        extra=0,
        can_delete=False)

    if request.method == 'POST':
        formset = InventoryFormSet(request.POST, instance=laptop)
        if formset.is_valid():
            formset.save()
            messages.success(
                request,
                f'Successfully updated inventory of {laptop}')
            return redirect(reverse('laptop_detail', args=[laptop.id]))

        else:
            messages.error(
                request,
                'Failed to update inventory. Please ensure the form is valid.'
                )
    else:
        formset = InventoryFormSet(instance=laptop)
        messages.info(request, f'You are editing the inventory of {laptop}.')

    template = 'products/edit_laptop_inventory.html'
    context = {
        'formset': formset,
        'laptop': laptop,
    }

    return render(request, template, context)


@login_required
def edit_phone_inventory(request, product_id):
    """
    A view for editing an existing Phone object's inventory objects.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    phone = get_object_or_404(Phone, pk=product_id)
    InventoryFormSet = inlineformset_factory(
        Product,
        Inventory,
        form=InventoryForm,
        extra=0,
        can_delete=False)

    if request.method == 'POST':
        formset = InventoryFormSet(request.POST, instance=phone)
        if formset.is_valid():
            formset.save()
            messages.success(
                request, f'Successfully updated inventory of {phone}'
                )
            return redirect(reverse('phone_detail', args=[phone.id]))

        else:
            messages.error(
                request,
                'Failed to update inventory. Please ensure the form is valid.'
                )

    else:
        formset = InventoryFormSet(instance=phone)
        messages.info(request, f'You are editing the inventory of {phone}.')

    template = 'products/edit_phone_inventory.html'
    context = {
        'formset': formset,
        'phone': phone,
    }

    return render(request, template, context)


@login_required
def edit_smartwatch_inventory(request, product_id):
    """
    A view for editing an existing Smartwatch object's inventory objects.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    smartwatch = get_object_or_404(Smartwatch, pk=product_id)
    InventoryFormSet = inlineformset_factory(
        Product, Inventory, form=InventoryForm, extra=0, can_delete=False
        )

    if request.method == 'POST':
        formset = InventoryFormSet(request.POST, instance=smartwatch)
        if formset.is_valid():
            formset.save()
            messages.success(
                request, f'Successfully updated inventory of {smartwatch}'
                )
            return redirect(
                reverse('smartwatch_detail', args=[smartwatch.id])
                )

        else:
            messages.error(
                request,
                'Failed to update inventory. Please ensure the form is valid.'
                )

    else:
        formset = InventoryFormSet(instance=smartwatch)
        messages.info(request, f'You are editing the inventory of {smartwatch}.')

    template = 'products/edit_smartwatch_inventory.html'
    context = {
        'formset': formset,
        'smartwatch': smartwatch,
    }

    return render(request, template, context)


@login_required
def edit_console_inventory(request, product_id):
    """
    A view for editing an existing Console object's inventory objects.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    console = get_object_or_404(Console, pk=product_id)
    InventoryFormSet = inlineformset_factory(
        Product, Inventory, form=InventoryForm, extra=0, can_delete=False)

    if request.method == 'POST':
        formset = InventoryFormSet(request.POST, instance=console)
        if formset.is_valid():
            formset.save()
            messages.success(
                request, f'Successfully updated inventory of {console}')
            return redirect(reverse('console_detail', args=[console.id]))

        else:
            messages.error(
                request,
                'Failed to update inventory. Please ensure the form is valid.'
                )

    else:
        formset = InventoryFormSet(instance=console)
        messages.info(request, f'You are editing the inventory of {console}.')

    template = 'products/edit_console_inventory.html'
    context = {
        'formset': formset,
        'console': console,
    }

    return render(request, template, context)


# view for deleting objects
@login_required
def delete_product(request, product_id):
    """
    A view for deleting objects.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
