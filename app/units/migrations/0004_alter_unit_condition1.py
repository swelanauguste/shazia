# Generated by Django 5.0.6 on 2024-06-12 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0003_unit_condition1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='condition1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='units.condition', verbose_name='condition'),
        ),
    ]
