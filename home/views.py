import random
from django.shortcuts import render, redirect, reverse
from products.models import Laptop
from .models import FAQ, Newsletter
from .forms import NewsletterForm
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_confirmation_email(email):
    subject = render_to_string('confirmation_emails/confirmation_email_subject.txt')
    body = render_to_string('confirmation_emails/confirmation_email_body.txt')
    send_mail(
        subject.strip(),
        body.strip(),
        settings.DEFAULT_FROM_EMAIL,
        [email],
    )

def index(request):
    laptops = list(Laptop.objects.filter(label='Gaming Laptop'))
    faqs = list(FAQ.objects.all())
    laptops = random.sample(laptops, 4)

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()
            messages.success(request, 'You have subscribed successfully!')
            send_confirmation_email(email)
            return redirect(reverse('home'))
    else:
        form = NewsletterForm()

    context = {
        'laptops': laptops,
        'faqs': faqs,
        'form': form,
    }

    return render(request, 'home/index.html', context)
