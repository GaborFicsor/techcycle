from django.shortcuts import render, redirect


def view_bag(request):
    """ A view to return the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):

    condition = request.POST.get('condition')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[item_id] = condition


    request.session['bag'] = bag
    return redirect(redirect_url)
