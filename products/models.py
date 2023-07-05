from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from django.db.models import Sum


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
    CHOICES = (
        ('acceptable', 'Acceptable'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
    )
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=8, null=True, blank=True, decimal_places=2)
    condition = models.CharField(max_length=20, choices=CHOICES, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    
    def name(self):
        return f"{self.brand} {self.series} {self.model}"

    def get_total_stock(self):
        return self.inventory.condition + self.inventory.stock_count

    def get_stock_status(self):
        total_stock = self.inventory.get_total_stock()
        if total_stock <= 2:
            return 'Low stock'
        elif total_stock == 0:
            return 'Out of stock'
        else:
            return 'In stock'

    def save(self, *args, **kwargs):
            is_new_product = not self.pk

            super().save(*args, **kwargs)

            if is_new_product:
                Inventory.objects.create(product=self, condition=self.condition, stock_count=1)



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


class Console(Product):
    storage_size = models.CharField(max_length=50)

class Inventory(models.Model):
    CONDITION_CHOICES = (
        ('acceptable', 'Acceptable'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    stock_count = models.PositiveIntegerField(default=0)

    def name(self):
        return f"{self.product.brand} {self.product.series} {self.product.model}"

    def __str__(self):
        return f"{self.condition}"

    def stock(self):
        return self.get_condition_display()

    def get_condition_display(self):
        return dict(self.CONDITION_CHOICES).get(self.condition)


    def increase_stock(self, quantity=1):
        self.stock_count += quantity
        self.save()

    def decrease_stock(self, quantity=1):
        if self.stock_count >= quantity:
            self.stock_count -= quantity
            self.save()

    def get_stock_count(self):
        return self.stock_count

@receiver(post_save, sender=Console)
def create_inventory(sender, instance, created, **kwargs):
    if created:
        Inventory.objects.create(console=instance)