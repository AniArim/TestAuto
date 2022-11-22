from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import *
from .serlializers import *


class BrandViewSet(viewsets.ModelViewSet):
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer

	@action(methods=['get'], detail=True)
	def models_for_brand(self, request, pk=None):
		try:
			brand = Brand.objects.get(pk=pk)
			models_list = Model.objects.filter(brand_id=pk)
			return Response({f'Models for {brand}': [i.title for i in models_list]})
		except ObjectDoesNotExist:
			return Response({f'models': 'Brand not found'})


class ColorViewSet(viewsets.ModelViewSet):
	queryset = Color.objects.all()
	serializer_class = ColorSerializer


class ModelViewSet(viewsets.ModelViewSet):
	queryset = Model.objects.all().select_related('brand')
	serializer_class = ModelSerializer

