from django.db.models import fields
from rest_framework import serializers
from .models import *


'''class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('date', 'color', 'get_brand', 'model', 'counter')'''


class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = Brand
		fields = ('pk', 'title',)


class ColorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Color
		fields = ('pk', 'title',)


class ModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Model
		fields = ('pk', 'title', 'brand')
