# Generated by Django 3.0.5 on 2020-06-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Birthday', 'Birthday'), ('Wedding', 'Wedding'), ('Anniversary', 'Anniversary'), ('New Home', 'New Home'), ('Baby', 'Baby')], max_length=100),
        ),
    ]
