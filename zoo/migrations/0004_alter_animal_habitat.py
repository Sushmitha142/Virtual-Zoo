# Generated by Django 5.1.4 on 2024-12-21 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0003_populate_animals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='habitat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to='zoo.habitat'),
        ),
    ]
