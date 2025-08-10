from django.db import models
from django.utils.translation import gettext_lazy as _

class Tool(models.Model):
    # This field stores user data. It will not be translated here.
    name = models.CharField(max_length=100)
    
    icon_class = models.CharField(max_length=50, help_text=_("e.g., 'fa-gavel' for a Font Awesome icon"))
    
    # This field stores user data. It will not be translated here.
    description = models.TextField()
    
    tool_url = models.URLField(max_length=200)
    
    status_choices = [
        ('LIVE', _('Live')), 
        ('SOON', _('Coming Soon'))
    ]
    status = models.CharField(max_length=4, choices=status_choices, default='LIVE')
    order = models.PositiveIntegerField(default=0, help_text=_("Used to order tools on the homepage"))

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Partner(models.Model):
    # This field stores user data. It will not be translated here.
    name = models.CharField(max_length=150)
    
    logo = models.ImageField(upload_to='partner_logos/')
    website_url = models.URLField(max_length=200, blank=True)
    
    tier_choices = [
        ('FOUNDING', _('Founding Partner')), 
        ('SUPPORT', _('Supporter'))
    ]
    tier = models.CharField(max_length=10, choices=tier_choices, default='SUPPORT')

    def __str__(self):
        return self.name

class ImpactMetric(models.Model):
    # This field stores user data. It will not be translated here.
    title = models.CharField(max_length=100, help_text=_("e.g., 'Users Helped'"))
    
    # This field stores user data. It will not be translated here.
    value = models.CharField(max_length=50, help_text=_("e.g., '10,000+'"))
    
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title