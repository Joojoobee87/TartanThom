# Generated by Django 3.0.5 on 2020-06-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_products_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Birthday', 'Birthday'), ('Wedding', 'Wedding'), ('Anniversary', 'Anniversary'), ('New Home', 'New Home'), ('Baby', 'Baby'), ('Leaving', 'Leaving')], max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(choices=[('A4', 'A4'), ('A5', 'A5'), ('200mm x 200mm', '200mm x 200mm'), ('122mm x 172mm', '122mm x 172mm'), ('172mm x 122mm', '172mm x 122mm'), ('250mm x 250mm', '250mm x 250mm'), ('210mm x 297mm', '210mm x 297mm'), ('152mm x variable', '152mm x variable')], max_length=100),
        ),
    ]