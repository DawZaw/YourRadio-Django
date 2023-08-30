# Generated by Django 4.2.4 on 2023-08-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='active_years',
            new_name='start_year',
        ),
        migrations.AddField(
            model_name='artist',
            name='end_year',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='photo',
            field=models.ImageField(default='static/img/default_artist.png', upload_to='artists/media/images/artists/'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(default='static/img/default_album.png', upload_to='artists/media/images/albums/'),
        ),
    ]