# Generated by Django 5.2.1 on 2025-05-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
