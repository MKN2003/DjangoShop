# Generated by Django 5.0.4 on 2024-04-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productsmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsmodel',
            name='category',
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='category',
            field=models.ManyToManyField(to='products.categorymodel'),
        ),
    ]
