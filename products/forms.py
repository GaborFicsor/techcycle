from django import forms
from .models import (
    Product, Category, Laptop, Phone, Smartwatch, Console, Inventory
    )
from .widgets import CustomClearableFileInput


class InventoryForm(forms.ModelForm):
    """
    Inventory form for handling stock count information.
    The disabled fields are not meant to be changed manually,
    as those are generated automatically.
    These are:
        - condition
        - price
        - sale price
    Form validation was added for the stock_count field
    """

    class Meta:
        model = Inventory
        fields = [
            'condition',
            'price',
            'sale_price',
            'stock_count',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['condition'].disabled = True
        self.fields['price'].disabled = True
        self.fields['sale_price'].disabled = True

    def clean_stock_count(self):
        stock_count = self.cleaned_data.get('stock_count')
        if stock_count > 99:
            raise forms.ValidationError('Stock count can only be 0-99')
        return stock_count


class LaptopForm(forms.ModelForm):
    """
    Laptop form for creating and editing Laptop objects.
    Form validation was added for the price field.
    """
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

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price > 2999:
            raise forms.ValidationError('Price should not be over 2999.')
        return price


class PhoneForm(forms.ModelForm):
    """
    Phone form for creating and editing Phone objects.
    Form validation was added for the price field.
    """
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

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price > 1499:
            raise forms.ValidationError('Price should not be over 1499.')
        return price


class SmartwatchForm(forms.ModelForm):
    """
    Smartwatch form for creating and editing Smartwatch objects.
    Form validation was added for the price field.
    """
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

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price > 999:
            raise forms.ValidationError('Price should not be over 999.')
        return price


class ConsoleForm(forms.ModelForm):
    """
    Console form for creating and editing Console objects.
    Form validation was added for the price field.
    """
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

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price > 599:
            raise forms.ValidationError('Price should not be over 599.')
        return price
