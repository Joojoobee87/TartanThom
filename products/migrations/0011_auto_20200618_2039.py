# Generated by Django 3.0.5 on 2020-06-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200618_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreviews',
            name='review_text',
            field=models.TextField(max_length=500),
        ),
    ]
