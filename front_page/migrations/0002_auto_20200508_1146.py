# Generated by Django 3.0.6 on 2020-05-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(),
        ),
    ]
