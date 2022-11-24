from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet)
router.register(r'color', ColorViewSet)
router.register(r'model', ModelViewSet)
router.register(r'order', OrderViewSet, basename='order')
router.register(r'order_create_up_del', OrderCreateUpdateDeleteViewSet, basename='order_create_up_del')
router.register(r'get_sum_of_cars_for_color', ColorFilterViewSet, basename='get_sum_of_cars_for_color')
router.register(r'get_sum_of_cars_for_model', ModelFilterViewSet, basename='get_sum_of_cars_for_model')

'''
API for brand filter http://127.0.0.1:8000/api/auto/order/?model=&counter_gt=&counter_lt=&brand=9&color=
'''

urlpatterns = [
	path('auto/', include(router.urls)),  # http://127.0.0.1:8000/api/auto/
]