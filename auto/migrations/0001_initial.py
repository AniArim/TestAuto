# Generated by Django 3.2 on 2022-11-22 03:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Марка автомобиля')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Цвет')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Модель автомобиля')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auto.brand', verbose_name='Марка')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(max_length=10, verbose_name='Номер заказа')),
                ('counter', models.PositiveIntegerField(max_length=100, verbose_name='Количество')),
                ('date', models.DateField(default=datetime.datetime(2022, 11, 22, 6, 49, 6, 699255), verbose_name='Дата заказа')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auto.color', verbose_name='Цвет')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auto.model', verbose_name='Модель')),
            ],
        ),
    ]
