# Generated by Django 2.2.16 on 2022-02-27 10:35

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220227_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[reviews.validators.less_then_now_year_validator]),
        ),
    ]