# Generated by Django 5.0.1 on 2024-03-15 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hostipal", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bloodbank", name="name", field=models.CharField(max_length=50),
        ),
    ]
