# Generated by Django 5.0.6 on 2024-08-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cover',
            field=models.ImageField(upload_to='item_covers/%Y/%m/%d/', verbose_name='Фото обложки'),
        ),
    ]