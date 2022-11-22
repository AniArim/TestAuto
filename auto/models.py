from datetime import datetime
from django.db import models


class Color(models.Model):
	title = models.CharField(max_length=100, verbose_name='Цвет')


class Brand(models.Model):
	title = models.CharField(max_length=120, verbose_name='Марка автомобиля')


class Model(models.Model):
	title = models.CharField(max_length=120, verbose_name='Модель автомобиля')
	brand = models.ForeignKey('Brand', on_delete=models.PROTECT, verbose_name='Марка')


class Order(models.Model):
	number = models.PositiveIntegerField(max_length=10, verbose_name='Номер заказа')
	color = models.ForeignKey('Color', on_delete=models.PROTECT, verbose_name='Цвет')
	model = models.ForeignKey('Model', on_delete=models.PROTECT, verbose_name='Модель')
	counter = models.PositiveIntegerField(max_length=100, verbose_name='Количество')
	date = models.DateField(default=datetime.now(), verbose_name='Дата заказа')




