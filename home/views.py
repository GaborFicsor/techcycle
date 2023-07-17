import random
from django.shortcuts import render, redirect, reverse
from products.models import Laptop
from .models import FAQ, Newsletter

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import NewsletterForm
from django.conf import settings


def send_confirmation_email(email):
    subject = render_to_string(
        'confirmation_emails/confirmation_email_subject.txt'
        )
    message = render_to_string(
        'confirmation_emails/confirmation_email_body.txt'
        )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email])


def index(request):
    laptops = list(Laptop.objects.filter(label='Gaming Laptop'))
    faqs = list(FAQ.objects.all())
    laptops = random.sample(laptops, 4)
    if request.method == 'POST':
        subscription_form = NewsletterForm(request.POST)
        if subscription_form.is_valid():
            email = subscription_form.cleaned_data['email']
            subscription_form.save()
            send_confirmation_email(email)
            messages.success(request, 'You have subscribed successfully!')
            return redirect('home')
    else:
        subscription_form = NewsletterForm()

    context = {
        'laptops': laptops,
        'subscription_form': subscription_form,
        'faqs': faqs,
    }
    return render(request, 'home/index.html', context)

def policy(request):
    return render(request, 'home/privacy_policy.html')

def conditions(request):
    return render(request, 'home/conditions.html')

def sustainability(request):
    return render(request, 'home/sustainability.html')

def inspections(request):
    return render(request, 'home/inspections.html')
