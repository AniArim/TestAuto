# Generated by Django 3.2 on 2022-11-22 05:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0002_auto_20221122_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата заказа'),
        ),
    ]
