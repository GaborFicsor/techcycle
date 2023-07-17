from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = [
            'email'
        ]
        
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'placeholder':'Your email address'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Newsletter.objects.filter(email=email).exists():
            raise forms.ValidationError('You are already subscribed.')
        return email
