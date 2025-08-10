from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(
        label=_('Your Name'), # Explicitly set and mark the label
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': _('Enter your full name')})
    )
    email = forms.EmailField(
        label=_('Your Email'), # Explicitly set and mark the label
        widget=forms.EmailInput(attrs={'class': 'form__input', 'placeholder': _('Enter your email address')})
    )
    subject = forms.CharField(
        label=_('Subject'), # Explicitly set and mark the label
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': _('The subject of your message')})
    )
    message = forms.CharField(
        label=_('Message'), # Explicitly set and mark the label
        widget=forms.Textarea(attrs={'class': 'form__textarea', 'placeholder': _('Your message')})
    )