from django import forms
from .models import Product, Category, Laptop, Phone, Smartwatch, Console, Inventory
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        firendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = firendly_names

class InventoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InventoryForm, self).__init__(*args, **kwargs)
        self.fields['condition'].disabled = True
        self.fields['price'].disabled = True
        self.fields['sale_price'].disabled = True

    class Meta:
        model = Inventory 
        fields = [
            'condition',
            'price',
            'sale_price',
            'stock_count',
        ]

class LaptopForm(forms.ModelForm):

    class Meta:
        model = Laptop
        fields = [
            'category',
            'brand',
            'series',
            'model',
            'color',
            'price',
            'sale',
            'sale_price',
            'image',
            'image_url',
            'label',
            'cpu_brand',
            'cpu_name',
            'ssd',
            'storage_size',
            'ram',
            'cpu_variant',
            'gpu',
            'cores',
            'os',
            'usb',
            'hdmi',
            'touchscreen',
            'dimensions',
            'weight',
            'finger_print_sensor',
            'keyboard',
            'backlit',
            'screen_size',
        ]

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PhoneForm(forms.ModelForm):

    class Meta:
        model = Phone
        fields = [
            'category',
            'brand',
            'series',
            'model',
            'color',
            'price',
            'sale',
            'sale_price',
            'image',
            'image_url',
            'sim',
            'cpu',
            'ram',
            'storage_size',
            'battery',
            'screen_size',
            'resolution',
            'camera_front',
            'camera_rear',
            'os',
        ]

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SmartwatchForm(forms.ModelForm):

    class Meta:
        model = Smartwatch
        fields = [
            'category',
            'brand',
            'series',
            'model',
            'color',
            'price',
            'sale',
            'sale_price',
            'image',
            'image_url',
            'connectivity',
            'display',
            'screen_size',
            'resolution',
            'water_resistance',
            'heart_rate_monitor',
            'gps',
            'os',
        ]


    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ConsoleForm(forms.ModelForm):

    class Meta:
        model = Console
        fields = [
            'category',
            'brand',
            'series',
            'model',
            'color',
            'price',
            'sale',
            'sale_price',
            'image',
            'image_url',
            'storage_size',
        ]

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
