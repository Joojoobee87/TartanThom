# Generated by Django 3.0.5 on 2020-06-26 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_auto_20200626_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='grade_total',
            new_name='grand_total',
        ),
    ]
