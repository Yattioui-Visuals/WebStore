# Generated by Django 3.2.9 on 2021-11-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_alter_orders_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default='IO', max_length=9),
        ),
    ]