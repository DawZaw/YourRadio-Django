# Generated by Django 4.2.4 on 2023-08-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_rename_album_slug_album_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(default='static/default_album.png', upload_to=''),
        ),
    ]
