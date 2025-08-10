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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Mark strings for translation
            full_subject = _("Contact Form Submission: %(subject)s") % {'subject': subject}
            message_intro = _("You have a new message from %(name)s (%(email)s).\n\nMessage:\n") % {'name': name, 'email': from_email}
            full_message = f"{message_intro}{message}"
            
            send_mail(
                subject=full_subject,
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.ADMIN_EMAIL],
            )
            
            return redirect(reverse('showcase:contact_success'))
    else:
        form = ContactForm()

    context = {
        'form': form
    }
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
