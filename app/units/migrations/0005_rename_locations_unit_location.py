# Generated by Django 5.0.6 on 2024-06-12 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0004_alter_unit_condition1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='locations',
            new_name='location',
        ),
    ]
