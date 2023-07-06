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

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    acceptable = models.BooleanField(default=False)
    good = models.BooleanField(default=False)
    excellent = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=8, null=True, blank=True, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    
    def save(self, *args, **kwargs):
            is_new = self.pk is None  # Check if it's a new object being created
            super().save(*args, **kwargs)
            
            if is_new:
                Inventory.objects.create(
                    product=self,
                    acceptable_amount=1 if self.acceptable else 0,
                    good_amount=1 if self.good else 0,
                    excellent_amount=1 if self.excellent else 0,
                )

            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.brand} {self.series} {self.model} | id:{self.id}"

    def available(self):
        if self.inventory.in_stock() > 0:
            return True
        return False
        
    available.boolean = True

    def on_sale(self):
        if self.sale:
            return True
        return False
        
    on_sale.boolean = True


    def in_stock(self):
        return self.inventory.acceptable_amount + self.inventory.good_amount + self.inventory.excellent_amount

    def acceptable(self):
        return self.inventory.acceptable_amount

    def good(self):
        return self.inventory.good_amount

    def excellent(self):
        return self.inventory.excellent_amount

    def conditions(self):
        conditions = []
        if self.inventory.acceptable_amount > 0:
            conditions.append("Acceptable")
        if self.inventory.good_amount > 0:
            conditions.append("Good")
        if self.inventory.excellent_amount > 0:
            conditions.append("Excellent")
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
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    acceptable_amount = models.PositiveIntegerField(default=0)
    good_amount = models.PositiveIntegerField(default=0)
    excellent_amount = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Inventories'

    def __str__(self):
        return f"{self.product.brand} {self.product.series} {self.product.model} - Inventory"

    def name(self):
        return f"{self.product.brand} {self.product.series} {self.product.model}"

    def in_stock(self):
        return self.acceptable_amount + self.good_amount + self.excellent_amount

