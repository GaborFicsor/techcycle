import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    Order model
    """
    order_number = models.CharField(
        max_length=32,
        null=False,
        editable=False
        )
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
        )
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
        )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
        )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False
        )
    country = CountryField(
        blank_label='Country *',
        null=False,
        blank=False
        )
    postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
        )
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
        )
    street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
        )
    street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )
    county = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )
    date = models.DateTimeField(
        auto_now_add=True
        )
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
        )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
        )
    original_bag = models.TextField(
        null=False,
        blank=False,
        default=''
        )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
        )

    def _generate_order_number(self):
        # generate a random string of 32 characters as an order number
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Order lineitem model with generated automatically
    generated fields during checkout process.
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
        )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    condition = models.CharField(
        max_length=10,
        null=True,
        blank=True
        )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
        )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
        null=False,
        blank=False,
        editable=False
        )
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False)

    """added price field to te orderlineitem,
    also added inventory and price to chekcout view
    where the orderlineitem is generated"""
    def save(self, *args, **kwargs):

        self.lineitem_total = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product}/{self.condition}'
        f'/{self.quantity}/{self.order.order_number}'
