from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Laptop(models.Model):

    CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

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

    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=8, null=True, blank=True, decimal_places=2)
    model = models.CharField(max_length=254)
    series = models.CharField(max_length=254)
    color = models.CharField(max_length=254)
    label = models.CharField(max_length=254)
    cpu_brand = models.CharField(max_length=254)
    cpu_name = models.CharField(max_length=254)
    ssd = models.CharField(max_length=254, choices=CHOICES)
    storage_size = models.CharField(max_length=254)
    ram = models.CharField(max_length=254)
    cpu_variant = models.CharField(max_length=254)
    gpu = models.CharField(max_length=254)
    cores = models.PositiveIntegerField(choices=CORES)
    os = models.CharField(max_length=254)
    usb = models.CharField(max_length=254)
    hdmi = models.CharField(max_length=254)
    touchscreen = models.CharField(max_length=254, choices=CHOICES)
    screen_size = models.PositiveIntegerField(choices=SIZES)
    dimensions = models.CharField(max_length=254)
    weight = models.CharField(max_length=254)
    finger_print_sensor = models.CharField(max_length=254, choices=CHOICES)
    keyboard = models.CharField(max_length=254)
    backlit = models.CharField(max_length=254, choices=CHOICES)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def set_sale_price(self, *args, **kwargs):
        if self.sale:
            self.sale_price = self.price * 0.95
        else:
            self.sale_price = None

    def __str__(self):
        return f'{self.brand} {self.series} {self.model}'

class Phone(models.Model):

    OS = [
        ('Android', 'Android'),
        ('iOS', 'iOS')
    ]
    
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=8, null=True, blank=True, decimal_places=2)
    series = models.CharField(max_length=254)
    model = models.CharField(max_length=254)
    sim = models.CharField(max_length=254)
    cpu = models.CharField(max_length=254)
    ram = models.CharField(max_length=254)
    storage_size = models.CharField(max_length=254)
    battery = models.CharField(max_length=254)
    screen_size = models.DecimalField(max_digits=4, decimal_places=2)
    resolution = models.CharField(max_length=254)
    camera_front = models.CharField(max_length=254)
    camera_rear = models.CharField(max_length=254)
    os = models.CharField(max_length=254, choices=OS)
    color = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return f'{self.brand} {self.series} {self.model}'

class Smartwatch(models.Model):

    CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=8, null=True, blank=True, decimal_places=2)
    series = models.CharField(max_length=254)
    model = models.CharField(max_length=254)
    connectivity = models.CharField(max_length=254)
    display = models.CharField(max_length=254)
    screen_size = models.DecimalField(max_digits=4, decimal_places=2)
    resolution = models.CharField(max_length=254)
    water_resistance = models.CharField(max_length=254)
    heart_rate_monitor = models.CharField(max_length=254, choices=CHOICES)
    gps = models.CharField(max_length=254, choices=CHOICES) 
    os = models.CharField(max_length=254)
    color = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return f'{self.brand} {self.series} {self.model}'

class Console(models.Model):

    BRAND = [
        ('Microsoft', 'Microsoft'),
        ('Sony', 'Sony'),
        ('Nintendo', 'Nintendo'),
    ]

    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=254, choices=BRAND)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=8, null=True, blank=True, decimal_places=2)
    series = models.CharField(max_length=254)
    model = models.CharField(max_length=254)
    storage_size = models.CharField(max_length=254)
    color = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return f'{self.brand} {self.series} {self.model}'