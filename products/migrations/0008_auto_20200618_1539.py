# Generated by Django 3.0.5 on 2020-06-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_products_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_bespoke',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]