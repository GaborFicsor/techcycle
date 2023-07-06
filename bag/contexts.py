from django.conf import settings
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        bag_items.append({
            'item_id': item_id,
            'condition': item_data,
            'product': product,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return context
