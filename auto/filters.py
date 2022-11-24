import django_filters
from django_filters import rest_framework as filters
from .models import *


class OrderFilter(filters.FilterSet):

	counter_gt = django_filters.NumberFilter(field_name='counter', lookup_expr='gt')
	counter_lt = django_filters.NumberFilter(field_name='counter', lookup_expr='lt')

	def __init__(self, *args, pk=None, **kwargs):
		super().__init__(*args, **kwargs)

	class Meta:
		model = Order
		fields = ['model', 'counter_gt', 'counter_lt', 'color', ]

