# Generated by Django 4.0.4 on 2022-06-17 00:25

from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_info_info_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='time',
            field=models.DateTimeField(default=timezone.now),
        ),
        migrations.AddField(
            model_name='bills',
            name='date',
            field=models.DateField(default=timezone.now),
        ),
        migrations.AddField(
            model_name='bills',
            name='namount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='bills',
            name='tamount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='charges',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='charges',
            name='time',
            field=models.DateTimeField(default=timezone.now),
        ),
    ]
