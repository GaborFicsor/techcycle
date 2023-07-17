from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from products.models import (
    Laptop, Phone, Smartwatch, Console, Category, Product, Inventory
    )
from django.contrib import messages


def view_bag(request):
    """
    A view for viewing the bag contents rendered in
    the bag.html template
    """
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
    """
    This view is used for adding products to the bag.
    We need to check what condition was selected for the product
    and then retrieve the price that belongs to that condition of
    the selected product.

    Also we need to check whether the selected product is already
    present in the bag with the same condition, and if so, we increment
    the quantity for that product, otherwise we just add the product
    with the selected condition and quantity.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    condition = request.POST.get('condition')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    item = request.session.get('item_id', {})
    selected_price = None

    for inventory in product.inventory_set.all():
        if inventory.condition == condition:
            selected_price = inventory.price

    if item_id in bag:
        item = bag[item_id]
        if condition in item:
            current_quantity = item[condition]['quantity']
            item[condition]['quantity'] += quantity
            messages.success(
                request,
                f'Added (+{quantity}) {product} ({condition})'
                f'to your cart ({current_quantity + quantity} in cart)')
        else:
            item[condition] = {'quantity': quantity}
            messages.success(
                request,
                f'Added ({quantity}) {product} ({condition}) to your cart'
                )
    else:
        item[condition] = {'quantity': quantity}
        messages.success(
            request,
            f'Added ({quantity}) {product} ({condition}) to your cart'
            )

    bag[item_id] = item
    request.session['bag'] = bag

    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """
    Removing an item removes all items from the bag
    with the same item_id and condition.
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        condition = request.POST['condition']
        bag = request.session.get('bag', {})
        quantity = bag[item_id][condition]['quantity']

        if condition:
            del bag[item_id][condition]
            if not bag[item_id]:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed ({quantity}) {product} ({condition}) from your cart'
                )

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
