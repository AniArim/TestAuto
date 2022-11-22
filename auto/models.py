from datetime import datetime
from django.db import models
from django.utils import timezone


class Color(models.Model):
	title = models.CharField(max_length=100, verbose_name='Цвет', unique=True)

	def __str__(self):
		return self.title


class Brand(models.Model):
	title = models.CharField(max_length=120, verbose_name='Марка автомобиля', unique=True)

	def __str__(self):
		return self.title


class Model(models.Model):
	title = models.CharField(max_length=120, verbose_name='Модель автомобиля', unique=True)
	brand = models.ForeignKey('Brand', on_delete=models.PROTECT, verbose_name='Марка')

	def __str__(self):
		return self.title


class Order(models.Model):
	number = models.PositiveIntegerField(verbose_name='Номер заказа')
	color = models.ForeignKey('Color', on_delete=models.PROTECT, verbose_name='Цвет')
	model = models.ForeignKey('Model', on_delete=models.PROTECT, verbose_name='Модель')
	counter = models.PositiveIntegerField(verbose_name='Количество')
	date = models.DateField(default=timezone.now, verbose_name='Дата заказа')

	def __str__(self):
		return self.number




