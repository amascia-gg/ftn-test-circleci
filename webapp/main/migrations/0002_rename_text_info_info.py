# Generated by Django 4.0.4 on 2022-06-17 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='text',
            new_name='info',
        ),
    ]