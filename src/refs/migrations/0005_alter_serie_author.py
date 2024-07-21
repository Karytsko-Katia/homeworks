# Generated by Django 5.0.6 on 2024-07-21 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refs', '0004_serie_author_alter_seriesprivately_series_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='series', to='refs.author'),
        ),
    ]