# Generated by Django 3.0.6 on 2020-05-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='price',
            field=models.IntegerField(),
        ),
    ]
