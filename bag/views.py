from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Laptop, Phone, Smartwatch, Console, Category, Product, Inventory
from django.contrib import messages


def view_bag(request):
    laptops = Laptop.objects.all()
    phones = Phone.objects.all()
    smartwatches = Smartwatch.objects.all()
    consoles = Console.objects.all()

    context = {
        'laptops': laptops,
        'phones': phones,
        'smartwatches': smartwatches,
        'consoles': consoles,
    }

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    condition = request.POST.get('condition')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    item = request.session.get('item_id', {})

    if item_id in bag:
        item = bag[item_id]

        if condition in item:
            current_quantity = item[condition]['quantity']
            item[condition]['quantity'] += quantity
            messages.success(request, f'Added ({quantity}) {product} ({condition}) to your cart ({current_quantity + quantity} in the cart)')
        else:
            item[condition] = {'quantity': quantity}
            messages.success(request, f'Added ({quantity}) {product} ({condition}) to your cart')
    else:
        item[condition] = {'quantity': quantity}
        messages.success(request, f'Added ({quantity}) {product} ({condition}) to your cart')

    bag[item_id] = item
    request.session['bag'] = bag

    print(request.session['bag'])
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    condition = request.POST['condition']
    bag = request.session.get('bag', {})


    del bag[item_id][condition]


    request.session['bag'] = bag
    return HttpResponse(status=200)
