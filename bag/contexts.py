from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    # initialize an empty bag if the current session does not have one
    bag_items = []
    total = Decimal('0')
    product_count = 0
    bag = request.session.get('bag', {})

    """
    for every item added to the bag, retrieve information for
    the item, it's condition, it's quantity and price,
    so that we can display it throughout the pages
    """

    for item_id, item_data in bag.items():
        for condition, quantity in item_data.items():
            item = get_object_or_404(Product, pk=item_id)
            inventory = item.inventory_set.get(condition=condition)
            # checking if the item is on salae
            if item.sale:
                price = inventory.sale_price
            else:
                price = inventory.price
            quantity = quantity['quantity']
            item_total = quantity * price
            total += item_total
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'condition': condition,
                'product': item,
                'price': price,
                'item_total': item_total,
            })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context
