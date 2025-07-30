from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=50, help_text="e.g., 'fa-gavel' for a Font Awesome icon")
    description = models.TextField()
    tool_url = models.URLField(max_length=200)
    status_choices = [('LIVE', 'Live'), ('SOON', 'Coming Soon')]
    status = models.CharField(max_length=4, choices=status_choices, default='LIVE')
    order = models.PositiveIntegerField(default=0, help_text="Used to order tools on the homepage")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='partner_logos/')
    website_url = models.URLField(max_length=200, blank=True)
    tier_choices = [('FOUNDING', 'Founding Partner'), ('SUPPORT', 'Supporter')]
    tier = models.CharField(max_length=10, choices=tier_choices, default='SUPPORT')

    def __str__(self):
        return self.name

class ImpactMetric(models.Model):
    title = models.CharField(max_length=100, help_text="e.g., 'Users Helped'")
    value = models.CharField(max_length=50, help_text="e.g., '10,000+'")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title