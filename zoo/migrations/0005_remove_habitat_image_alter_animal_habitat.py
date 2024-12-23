# Generated by Django 5.1.4 on 2024-12-22 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0004_alter_animal_habitat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitat',
            name='image',
        ),
        migrations.AlterField(
            model_name='animal',
            name='habitat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zoo.habitat'),
        ),
    ]