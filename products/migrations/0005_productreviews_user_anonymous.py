# Generated by Django 3.0.5 on 2020-05-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200518_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreviews',
            name='user_anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
