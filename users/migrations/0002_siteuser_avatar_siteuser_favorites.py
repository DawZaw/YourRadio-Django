# Generated by Django 4.2.4 on 2023-08-31 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='avatar',
            field=models.ImageField(default='static/img/default_user.png', upload_to='users/media/images/avatars/'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='favorites',
            field=models.ManyToManyField(to='artists.album'),
        ),
    ]
