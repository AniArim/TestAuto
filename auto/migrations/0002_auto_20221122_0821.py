# Generated by Django 3.2 on 2022-11-22 05:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(max_length=120, unique=True, verbose_name='Марка автомобиля'),
        ),
        migrations.AlterField(
            model_name='color',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='model',
            name='title',
            field=models.CharField(max_length=120, unique=True, verbose_name='Модель автомобиля'),
        ),
        migrations.AlterField(
            model_name='order',
            name='counter',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 22, 5, 21, 44, 800308, tzinfo=utc), verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.PositiveIntegerField(verbose_name='Номер заказа'),
        ),
    ]
