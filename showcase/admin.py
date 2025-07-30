from django.contrib import admin
from .models import Tool, Partner, ImpactMetric

admin.site.register(Tool)
admin.site.register(Partner)
admin.site.register(ImpactMetric)