# Generated by Django 5.0.1 on 2024-03-13 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientregistermodel",
            name="height",
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
