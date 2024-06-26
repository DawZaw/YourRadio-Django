# Generated by Django 4.2.4 on 2023-08-31 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover', models.ImageField(default='static/img/default_album.png', upload_to='artists/media/images/albums/')),
                ('release_date', models.DateField()),
                ('slug', models.SlugField(allow_unicode=True, max_length=100)),
            ],
            options={
                'ordering': ['release_date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_year', models.DateField()),
                ('end_year', models.DateField(blank=True, default=None, null=True)),
                ('photo', models.ImageField(default='static/img/default_artist.png', upload_to='artists/media/images/artists/')),
                ('type', models.CharField(choices=[('b', 'Band'), ('s', 'Solo Artist')], help_text='Artist type (Band, Solo)', max_length=1)),
                ('slug', models.SlugField(allow_unicode=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('length', models.DurationField(default=0)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album', to='artists.artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(to='artists.genre'),
        ),
    ]
