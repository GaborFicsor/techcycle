from django.shortcuts import render, redirect
from products.models import Laptop, Phone, Smartwatch, Console, Category, Product, Inventory


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
    quantity = int(request.POST.get('quantity'))
    condition = request.POST.get('condition')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        item = bag[item_id]
        if condition in item:
            item[condition]['quantity'] += quantity
        else:
            item[condition] = {'quantity': quantity}
    else:
        item = {condition: {'quantity': quantity}}

    bag[item_id] = item
    request.session['bag'] = bag

    print(request.session['bag'])
    return redirect(redirect_url)

