from datetime import date
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
	brand = models.ForeignKey('Brand', on_delete=models.PROTECT, verbose_name='Марка', related_name='brands')

	def __str__(self):
		return self.title


class Order(models.Model):

	color = models.ForeignKey('Color', on_delete=models.PROTECT, verbose_name='Цвет авто', related_name='colors')
	model = models.ForeignKey('Model', on_delete=models.PROTECT, verbose_name='Модель', related_name='models')
	counter = models.PositiveIntegerField(verbose_name='Количество')
	date = models.DateField(default=date.today, verbose_name='Дата заказа')

	def __str__(self):
		return str(self.pk)





