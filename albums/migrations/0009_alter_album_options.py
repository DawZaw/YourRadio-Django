# Generated by Django 4.2.4 on 2023-08-18 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0008_alter_album_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['release_date', 'title']},
        ),
    ]
