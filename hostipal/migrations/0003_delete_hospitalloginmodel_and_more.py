# Generated by Django 5.0.1 on 2024-03-18 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hostipal", "0002_alter_bloodbank_name"),
    ]

    operations = [
        migrations.DeleteModel(name="hospitalloginmodel",),
        migrations.RemoveField(model_name="hospitalregistermodel", name="password",),
        migrations.RemoveField(model_name="hospitalregistermodel", name="username",),
    ]