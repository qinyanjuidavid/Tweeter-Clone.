# Generated by Django 3.0.5 on 2020-04-10 19:48

from django.db import migrations, models
import tweeter.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(max_length=250, validators=[tweeter.models.validate_content]),
        ),
    ]