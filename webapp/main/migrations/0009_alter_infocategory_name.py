# Generated by Django 4.0.4 on 2022-06-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_infocategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infocategory',
            name='name',
            field=models.TextField(default='', max_length=30),
        ),
    ]