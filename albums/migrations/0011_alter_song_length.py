# Generated by Django 4.2.4 on 2023-08-21 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0010_remove_song_pos_remove_song_slug_song_length_song_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='length',
            field=models.DurationField(default=0),
        ),
    ]
