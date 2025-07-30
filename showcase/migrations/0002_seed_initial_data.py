# In showcase/migrations/0002_seed_initial_data.py

from django.db import migrations

def seed_initial_data(apps, schema_editor):
    """
    Seeds the database with the initial content for Tools,
    Impact Metrics, and Partners.
    """
    # Get the model from the historical app registry
    Tool = apps.get_model('showcase', 'Tool')
    ImpactMetric = apps.get_model('showcase', 'ImpactMetric')
    Partner = apps.get_model('showcase', 'Partner')

    # --- Create Impact Metrics ---
    ImpactMetric.objects.create(
        title="Tax Calculations Done (since July 1, 2025)",
        value="58",
        order=0
    )
    ImpactMetric.objects.create(
        title="Letters of Demand Generated (since July 1, 2025)",
        value="3",
        order=1
    )

    # --- Create Tools ---
    Tool.objects.create(
        name="Comprehensive Tax Calculator",
        icon_class="calculate",
        description="A comprehensive tax calculator, home office expense calculation, and a chatbot linked to all tax legislation.",
        tool_url="https://tax.amicus-law.com",
        status="LIVE",
        order=0
    )
    Tool.objects.create(
        name="Small Claims Navigator",
        icon_class="gavel",
        description="Generates a Letter of Demand and will eventually help with the whole small claims journey.",
        tool_url="https://smallclaims.rosetta-returns.co.za",
        status="LIVE",
        order=1
    )
    Tool.objects.create(
        name="Labour Law Bot",
        icon_class="chat",
        description="An AI-powered chatbot to help you with your labour law questions.",
        tool_url="https://amicus-law.com",
        status="LIVE",
        order=2
    )

    # --- Create Partners ---
    # Note: The logo field will be empty. It must be added manually via the admin
    # as the migration doesn't have access to image files.
    Partner.objects.create(
        name="Amicus Legaltech",
        website_url="https://amicus-law.com",
        tier="FOUNDING"
    )

def remove_initial_data(apps, schema_editor):
    """
    Removes the data we seeded. This makes the migration reversible.
    """
    Tool = apps.get_model('showcase', 'Tool')
    ImpactMetric = apps.get_model('showcase', 'ImpactMetric')
    Partner = apps.get_model('showcase', 'Partner')

    Tool.objects.filter(name__in=[
        "Comprehensive Tax Calculator",
        "Small Claims Navigator",
        "Labour Law Bot"
    ]).delete()

    ImpactMetric.objects.filter(title__startswith="Tax Calculations Done").delete()
    ImpactMetric.objects.filter(title__startswith="Letters of Demand Generated").delete()

    Partner.objects.filter(name="Amicus Legaltech").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_initial_data, reverse_code=remove_initial_data),
    ]