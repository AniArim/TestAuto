from django.urls import path, include
from django.views.generic import TemplateView

from .views import *
from rest_framework import routers

from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet)
router.register(r'color', ColorViewSet)
router.register(r'model', ModelViewSet)
router.register(r'order', OrderViewSet, basename='order')
router.register(r'order_create_up_del', OrderCreateUpdateDeleteViewSet, basename='order_create_up_del')
router.register(r'get_sum_of_cars_for_color', ColorFilterViewSet, basename='get_sum_of_cars_for_color')
router.register(r'get_sum_of_cars_for_model', ModelFilterViewSet, basename='get_sum_of_cars_for_model')


schema_view = get_schema_view(
	openapi.Info(
		title='API для тестового задания',
		default_version='0.0.1',
		description='Some description',
		contact=openapi.Contact(email='ekb.iab@yandex.ru', name='Admin')
	),
	patterns=[path('api/', include('auto.urls')), ],
	public=True,
)


'''
Фильтрация списка заказов по марке авто:
 http://127.0.0.1:8000/api/auto/order/?model=&counter_gt=&counter_lt=&brand=9&color=
'''

urlpatterns = [
	path(
		'swagger-ui/',
		TemplateView.as_view(
			template_name='swaggerui/swaggerui.html',
			extra_context={'schema_url': 'openapi-schema'}
		),
		name='swagger-ui'),
	url(
		r'^swagger(?P<format>\.json|\.yaml)$',
		schema_view.without_ui(cache_timeout=0),
		name='schema-json'
	),
	path('auto/', include(router.urls)),  # http://127.0.0.1:8000/api/auto/

]