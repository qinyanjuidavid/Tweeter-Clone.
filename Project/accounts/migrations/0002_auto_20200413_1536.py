# Generated by Django 3.0.5 on 2020-04-13 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='date_of_birth',
            new_name='birth_date',
        ),
    ]