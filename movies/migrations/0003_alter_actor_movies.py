# Generated by Django 3.2.3 on 2021-05-26 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(related_name='actor', to='movies.Movie'),
        ),
    ]