# Generated by Django 3.1 on 2020-09-02 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Year', models.IntegerField(blank=True)),
                ('Rated', models.CharField(blank=True, max_length=10)),
                ('Released', models.DateField(blank=True)),
                ('Runtime', models.CharField(blank=True, max_length=25)),
                ('Director', models.CharField(blank=True, max_length=100)),
                ('Writer', models.CharField(blank=True, max_length=300)),
                ('Plot', models.CharField(blank=True, max_length=900)),
                ('Language', models.CharField(blank=True, max_length=300)),
                ('Country', models.CharField(blank=True, max_length=250)),
                ('Awards', models.CharField(blank=True, max_length=250)),
                ('Poster', models.ImageField(blank=True, upload_to='movies')),
                ('Metascore', models.CharField(blank=True, max_length=5)),
                ('imdbRating', models.CharField(blank=True, max_length=5)),
                ('imdbVotes', models.IntegerField(blank=True)),
                ('imdbID', models.CharField(blank=True, max_length=100)),
                ('Type', models.CharField(blank=True, max_length=10)),
                ('DVD', models.DateField(blank=True)),
                ('boxOffice', models.IntegerField(blank=True)),
                ('Production', models.CharField(blank=True, max_length=100)),
                ('Website', models.CharField(blank=True, max_length=150)),
                ('totalSeasons', models.CharField(blank=True, max_length=3)),
                ('Actors', models.ManyToManyField(blank=True, to='movie.Actor')),
                ('Genre', models.ManyToManyField(blank=True, to='movie.Genre')),
                ('Ratings', models.ManyToManyField(blank=True, to='movie.Rating')),
            ],
        ),
    ]
