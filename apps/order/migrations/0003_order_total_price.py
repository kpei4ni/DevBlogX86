# Generated by Django 5.0.2 on 2024-04-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=9999999, max_digits=10, verbose_name='Total price'),
        ),
    ]
