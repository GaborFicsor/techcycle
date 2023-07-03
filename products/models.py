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
    CHOICES = (
        ('acceptable', 'Acceptable'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
    )
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
    stock_acceptable = models.PositiveIntegerField(default=0)
    stock_good = models.PositiveIntegerField(default=0)
    stock_excellent = models.PositiveIntegerField(default=0)
    
    def get_total_stock(self):
            return self.stock_acceptable + self.stock_good + self.stock_excellent

    def get_stock_status(self):
        total_stock = self.get_total_stock()
        if total_stock <= 2:
            return 'Low stock'
        elif total_stock == 0:
            return 'Out of stock'
        else:
            return 'In stock'
            
    def save(self, *args, **kwargs):
        # Check the condition of the product
        condition = self.condition
        
        # Increment the corresponding stock field based on the condition
        if condition:
            if condition == 'acceptable':
                self.stock_acceptable += 1
            elif condition == 'good':
                self.stock_good += 1
            elif condition == 'excellent':
                self.stock_excellent += 1

        self.sale_price = self.price * Decimal('0.95')
        super().save(*args, **kwargs)


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

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
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
    
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
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

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    connectivity = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    screen_size = models.DecimalField(max_digits=4, decimal_places=2)
    resolution = models.CharField(max_length=50)
    water_resistance = models.CharField(max_length=50)
    heart_rate_monitor = models.BooleanField(default=False)
    gps = models.BooleanField(default=False)
    os = models.CharField(max_length=50)



class Console(Product):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    storage_size = models.CharField(max_length=50)

# @receiver(post_save, sender=Product)
# def update_stock(sender, instance, **kwargs):
#     # Retrieve the selected condition for the product
#     condition_name = instance.condition.name

#     # Update the stock for the selected condition
#     condition = Condition.objects.get(name=condition_name)
#     condition.stock += 1
#     condition.save()
