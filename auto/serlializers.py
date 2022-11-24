from django.db.models import Sum
from rest_framework import serializers
from .models import *


class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = Brand
		fields = ('pk', 'title',)


class ColorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Color
		fields = ('pk', 'title',)


class ColorFilterSerializer(serializers.ModelSerializer):
	sum_of_cars = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Color
		fields = ('title',  'sum_of_cars')

	def get_sum_of_cars(self, obj):
		order = Order.objects.filter(color=obj)
		sum_of_cars_for_color = (order.aggregate(Sum('counter'))).get('counter__sum')
		return sum_of_cars_for_color


class ModelFilterSerializer(serializers.ModelSerializer):
	sum_of_cars = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Model
		fields = ('title',  'sum_of_cars')

	def get_sum_of_cars(self, obj):
		order = Order.objects.filter(model=obj)
		sum_of_cars_for_model = (order.aggregate(Sum('counter'))).get('counter__sum')
		return sum_of_cars_for_model


class ModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Model
		fields = ('pk', 'title', 'brand')


class OrderSerializer(serializers.ModelSerializer):
	model = serializers.SerializerMethodField(read_only=True)
	brand = serializers.SerializerMethodField(read_only=True)
	color = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Order
		fields = ('pk', 'number', 'date', 'color', 'counter', 'model', 'brand')

	def get_model(self, obj):
		model = obj.model
		serializer = ModelSerializer(model, many=False)
		print(serializer.data, 'get_model function <----------------->')
		return serializer.data

	def get_brand(self, obj):
		brand_id = obj.model.brand
		serializer = BrandSerializer(brand_id, many=False)
		print(serializer.data, 'get_brand function <----------------->')
		return serializer.data

	def get_color(self, obj):
		model = obj.color
		serializer = ColorSerializer(model, many=False)
		print(serializer.data, 'get_color function <----------------->')
		return serializer.data


class OrderForCreateDelUpSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('pk', 'number', 'date', 'color', 'counter',  'model',)
