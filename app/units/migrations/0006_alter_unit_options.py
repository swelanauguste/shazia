# Generated by Django 5.0.6 on 2024-06-12 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0005_rename_locations_unit_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['description']},
        ),
    ]
