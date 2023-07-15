from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=8, null=True, blank=True, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def name(self):
        return f"{self.brand} {self.series} {self.model}"

    def lowest_price(self):
        prices = self.inventory_set.filter(stock_count__gt=0).values_list('price', flat=True)
        if prices:
            lowest_price = min(prices)
            return Decimal(lowest_price)
        else:
            return 'Out of stock'

    def lowest_sale_price(self):
        sale_prices = self.inventory_set.filter(stock_count__gt=0).values_list('sale_price', flat=True)
        if sale_prices:
            lowest_sale_price = min(sale_prices)
            return Decimal(lowest_sale_price)
        else:
            return 'Out of stock'

    def save(self, *args, **kwargs):
        is_new_product = not self.pk
        if is_new_product:
            price = Decimal(self.price)
            super().save(*args, **kwargs)
            Inventory.objects.create(
            product=self,
            condition='acceptable',
            price = self.price * Decimal('0.8'),
            sale_price = price * Decimal('0.95'),
            )
            Inventory.objects.create(
            product=self,
            condition='good',
            price = self.price * Decimal('0.9'),
            sale_price = price * Decimal('0.95'),
            )
            Inventory.objects.create(
            product=self,
            condition='excellent',
            price=self.price,
            sale_price=price * Decimal('0.95'),
            )
        else:
            # Update inventory prices
            old_product = Product.objects.get(pk=self.pk)
            price_changed = self.price != old_product.price

            super().save(*args, **kwargs)

            if price_changed:
                inventory_objects = Inventory.objects.filter(product=self)
                for inventory in inventory_objects:
                    if inventory.condition == 'acceptable':
                        inventory.price = self.price * Decimal('0.8')
                        inventory.sale_price = inventory.price * Decimal('0.95')
                    elif inventory.condition == 'good':
                        inventory.price = self.price * Decimal('0.9')
                        inventory.sale_price = inventory.price * Decimal('0.95')
                    elif inventory.condition == 'excellent':
                        inventory.price = self.price
                        inventory.sale_price = inventory.price * Decimal('0.95')
                    inventory.save()

    def __str__(self):
        return f"{self.brand} {self.series} {self.model}"

    def available(self):
        inventory_objects = self.inventory_set.all()

        for inventory in inventory_objects:
            if inventory.stock_count > 0:
                return True

        return False

    available.boolean = True
    def on_sale(self):
        if self.sale:
            return True
        return False

    on_sale.boolean = True
    def in_stock(self):
        inventory_objects = self.inventory_set.all()
        stock_amount = 0

        for inventory in inventory_objects:
            if inventory.condition == 'acceptable':
                stock_amount += inventory.stock_count
            elif inventory.condition == 'good':
                stock_amount += inventory.stock_count
            elif inventory.condition == 'excellent':
                stock_amount += inventory.stock_count

        return stock_amount

    def acceptable(self):
        return self.inventory.acceptable_amount

    def good(self):
        return self.inventory.good_amount

    def excellent(self):
        return self.inventory.excellent_amount

    def conditions(self):
        inventory_objects = self.inventory_set.all()
        conditions = []

        for inventory in inventory_objects:
            if inventory.stock_count > 0:
                conditions.append(inventory.get_condition_display())

        return conditions

class Laptop(Product):

    SIZES = [
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17)
    ]

    CORES = [
        (2, 2),
        (4, 4),
        (6, 6),
        (8, 8),
        (10, 10),
        (12, 12)
    ]

    label = models.CharField(max_length=50)
    cpu_brand = models.CharField(max_length=50)
    cpu_name = models.CharField(max_length=50)
    ssd = models.BooleanField(default=False)
    storage_size = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    cpu_variant = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    cores = models.PositiveIntegerField(choices=CORES)
    os = models.CharField(max_length=50)
    usb = models.CharField(max_length=50)
    hdmi = models.CharField(max_length=50)
    touchscreen = models.BooleanField(default=False)
    screen_size = models.PositiveIntegerField(choices=SIZES)
    dimensions = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    finger_print_sensor = models.BooleanField(default=False)
    keyboard = models.CharField(max_length=50)
    backlit = models.BooleanField(default=False)

    def name(self):
        return f"{self.brand} {self.series} {self.model}"

    def cpu(self):
        return f"{self.cpu_brand} {self.cpu_name} {self.cpu_variant}"

class Phone(Product):

    OS = [
        ('Android', 'Android'),
        ('iOS', 'iOS')
    ]

    sim = models.CharField(max_length=50)
    cpu = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    storage_size = models.CharField(max_length=50)
    battery = models.CharField(max_length=50)
    screen_size = models.DecimalField(max_digits=4, decimal_places=2)
    resolution = models.CharField(max_length=50)
    camera_front = models.CharField(max_length=50)
    camera_rear = models.CharField(max_length=50)
    os = models.CharField(max_length=50, choices=OS)

    def name(self):
        return f"{self.brand} {self.series} {self.model}"

class Smartwatch(Product):

    class Meta:
        verbose_name_plural = 'Smartwatches'

    connectivity = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    screen_size = models.DecimalField(max_digits=4, decimal_places=2)
    resolution = models.CharField(max_length=50)
    water_resistance = models.CharField(max_length=50)
    heart_rate_monitor = models.BooleanField(default=False)
    gps = models.BooleanField(default=False)
    os = models.CharField(max_length=50)

    def name(self):
        return f"{self.brand} {self.series} {self.model}"

class Console(Product):
    storage_size = models.CharField(max_length=50)

    def name(self):
        return f"{self.brand} {self.series} {self.model}"

class Inventory(models.Model):
    CONDITION_CHOICES = (
        ('acceptable', 'Acceptable'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    sale_price = models.DecimalField(max_digits=8, null=True, blank=True, decimal_places=2, default=0)
    stock_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Inventories'

    def __str__(self):
        return f"{self.product.brand} {self.product.series} {self.product.model} - Inventory"

    def name(self):
        return f"{self.product.brand} {self.product.series} {self.product.model}"

    def in_stock(self):
        return self.acceptable_amount + self.good_amount + self.excellent_amount

