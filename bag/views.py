from django.shortcuts import render, redirect


def view_bag(request):
    """ A view to return the bag contents page """

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

