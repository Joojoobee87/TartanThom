# Generated by Django 3.0.5 on 2020-06-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_bespoke_bespoke_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bespoke',
            name='is_complete',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
