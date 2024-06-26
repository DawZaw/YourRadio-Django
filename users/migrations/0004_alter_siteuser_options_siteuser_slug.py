# Generated by Django 5.0.4 on 2024-04-12 13:12

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_siteuser_options_remove_siteuser_favorites_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='siteuser',
            options={'ordering': [django.db.models.functions.text.Lower('username')]},
        ),
        migrations.AddField(
            model_name='siteuser',
            name='slug',
            field=models.SlugField(default='user'),
        ),
    ]
