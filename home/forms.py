from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = [
            'email'
        ]

    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'placeholder':'Your email address'}))

