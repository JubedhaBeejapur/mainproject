# Generated by Django 5.0.1 on 2024-03-18 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hostipal", "0003_delete_hospitalloginmodel_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="hospitalhomemodel", name="image",),
    ]
