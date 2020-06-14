# Generated by Django 3.0.5 on 2020-06-14 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20200614_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bespoke',
            name='bespoke_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order'),
        ),
    ]
