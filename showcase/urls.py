# showcase/urls.py

from django.urls import path
from . import views

app_name = 'showcase'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('partners/', views.partners, name='partners'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]