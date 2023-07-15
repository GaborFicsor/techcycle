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
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

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

    def clean_stock_count(self):
        stock_count = self.cleaned_data.get('stock_count')
        if stock_count > 99:
            raise forms.ValidationError('Stock count can only be 0-99')
        return stock_count

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

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price > 2999:
            raise forms.ValidationError('Price should not be over 2999.')
        return price


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

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price > 1499:
            raise forms.ValidationError('Price should not be over 1499.')
        return price


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

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price > 999:
            raise forms.ValidationError('Price should not be over 999.')
        return price


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

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price > 599:
            raise forms.ValidationError('Price should not be over 599.')
        return price
