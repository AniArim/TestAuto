from django.db.models import Sum
from rest_framework import serializers
from .models import *


class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = Brand
		fields = ('title',)


class ColorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Color
		fields = ('title',)


class ColorFilterSerializer(serializers.ModelSerializer):
	sum_of_cars = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Color
		fields = ('title',  'sum_of_cars')

	def get_sum_of_cars(self, obj):
		order = Order.objects.all().select_related('model').select_related('color').filter(color=obj)
		sum_of_cars_for_color = (order.aggregate(Sum('counter'))).get('counter__sum')
		return sum_of_cars_for_color


class ModelFilterSerializer(serializers.ModelSerializer):
	sum_of_cars = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Model
		fields = ('title',  'sum_of_cars')

	def get_sum_of_cars(self, obj):
		order = Order.objects.all().select_related('model').select_related('color').filter(model=obj)
		sum_of_cars_for_model = (order.aggregate(Sum('counter'))).get('counter__sum')
		return sum_of_cars_for_model


class ModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Model
		fields = ('title', 'brand')


class OrderSerializer(serializers.ModelSerializer):
	model = serializers.SerializerMethodField(read_only=True)
	brand = serializers.SerializerMethodField(read_only=True)
	color = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Order
		fields = ('date', 'color', 'counter', 'model', 'brand')

	def get_model(self, obj):
		model = obj.model
		return model.title

	def get_brand(self, obj):
		brand = obj.model.brand
		return brand.title

	def get_color(self, obj):
		color = obj.color
		return color.title


class OrderForCreateDelUpSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('date', 'color', 'counter',  'model',)
