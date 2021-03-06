# Generated by Django 3.0.5 on 2020-06-13 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200612_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreviews',
            name='review_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='label',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Sale', 'Sale')], max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
