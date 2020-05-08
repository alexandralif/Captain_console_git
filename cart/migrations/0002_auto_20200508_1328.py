# Generated by Django 3.0.6 on 2020-05-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_page', '0002_auto_20200508_1146'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='computer_products',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='game_products',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='front_page.products'),
        ),
    ]
