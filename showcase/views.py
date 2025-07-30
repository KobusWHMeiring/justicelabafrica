# In showcase/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .models import Tool, Partner, ImpactMetric
from .forms import ContactForm 
# ... (home, about, partners views remain unchanged) ...

def contact(request):
    """
    View for the 'Contact' page. Handles form submission.
    """
    print("Contact view accessed")
    if request.method == 'POST':
        # This part handles after you click "submit"
        form = ContactForm(request.POST)
        if form.is_valid():
            # (All your email sending logic is here)
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_subject = f"Contact Form Submission: {subject}"
            full_message = f"You have a new message from {name} ({from_email}).\n\n" \
                           f"Message:\n{message}"
            
            send_mail(
                subject=full_subject,
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.ADMIN_EMAIL],
            )
            
            return redirect(reverse('showcase:contact_success'))
    else:
        # ---- THIS IS THE CRUCIAL PART FOR DISPLAYING THE FORM ----
        # This part runs when you first visit the page.
        form = ContactForm()

    # ---- AND THIS PART IS ALSO CRUCIAL ----
    # This must be outside the if/else, so it runs for both cases
    context = {
        'form': form
    }
    print(context)
    return render(request, 'showcase/contact.html', context)

def contact_success(request):
    """
    View for the page shown after successful contact form submission.
    """
    return render(request, 'showcase/contact_success.html')

def home(request):
    """
    View for the homepage. Fetches all necessary dynamic content.
    """
    tools = Tool.objects.all()
    partners = Partner.objects.all()
    impact_metrics = ImpactMetric.objects.all()

    context = {
        'tools': tools,
        'partners': partners,
        'impact_metrics': impact_metrics,
    }
    return render(request, 'showcase/home.html', context)

def about(request):
    """
    View for the static 'About' page.
    """
    return render(request, 'showcase/about.html')

def partners(request):
    """
    View for the 'Partners' page. Fetches all partners.
    """
    all_partners = Partner.objects.all()
    context = {
        'all_partners': all_partners,
    }
    return render(request, 'showcase/partners.html', context)
