
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response

from .filters import *
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


class ColorFilterViewSet(viewsets.mixins.ListModelMixin,
                         viewsets.mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):

	serializer_class = ColorFilterSerializer
	queryset = Color.objects.all()


class ModelFilterViewSet(viewsets.mixins.ListModelMixin,
                         viewsets.mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):

	serializer_class = ModelFilterSerializer
	queryset = Model.objects.all()


class ModelViewSet(viewsets.ModelViewSet):
	queryset = Model.objects.all().select_related('brand')
	serializer_class = ModelSerializer


class OrderViewSet(viewsets.mixins.ListModelMixin,
                   viewsets.mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

	serializer_class = OrderSerializer
	filterset_class = OrderFilter

	def get_queryset(self):
		brand = self.request.query_params.get('brand', )
		if brand:
			temp = Model.objects.all().select_related('brand').filter(brand_id=brand)
			orders_list = []
			for i in temp:
				orders = Order.objects.filter(model_id=i.pk)
				for item in orders:
					orders_list.append(item.pk)
			return Order.objects.filter(pk__in=orders_list)
		else:
			return Order.objects.all().select_related('model').select_related('color')


class OrderCreateUpdateDeleteViewSet(viewsets.mixins.CreateModelMixin,
                                     viewsets.mixins.RetrieveModelMixin,
                                     viewsets.mixins.UpdateModelMixin,
                                     viewsets.mixins.DestroyModelMixin,
                                     viewsets.GenericViewSet):

	queryset = Order.objects.all().select_related('model').select_related('color')
	serializer_class = OrderForCreateDelUpSerializer
