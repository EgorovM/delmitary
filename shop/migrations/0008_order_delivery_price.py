# Generated by Django 3.2.8 on 2021-12-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_order_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_price',
            field=models.IntegerField(default=0),
        ),
    ]
