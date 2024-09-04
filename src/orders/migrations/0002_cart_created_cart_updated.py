# Generated by Django 5.0.6 on 2024-08-31 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 8, 31, 19, 56, 43, 440527, tzinfo=datetime.timezone.utc), verbose_name='Created date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificate date'),
        ),
    ]