# Generated by Django 4.0.4 on 2022-06-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_infocategory_image_infocategory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infocategory',
            name='name',
            field=models.TextField(default=''),
        ),
    ]