# Generated by Django 3.0 on 2020-07-26 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='lastname',
        ),
    ]
