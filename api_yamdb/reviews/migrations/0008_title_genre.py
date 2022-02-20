# Generated by Django 2.2.16 on 2022-02-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20220220_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(through='reviews.GenreTitle', to='reviews.Genre'),
        ),
    ]