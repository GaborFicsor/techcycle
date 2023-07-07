from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = Decimal('0')
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        for condition, quantity in item_data.items():
            quantity = quantity['quantity']
            product = get_object_or_404(Product, pk=item_id)
            item_total = quantity * product.price
            total += item_total
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'condition': condition,
                'product': product,
                'item_total': item_total,
            })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }
    # print(bag)
    return context
