from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet)
router.register(r'color', ColorViewSet)
router.register(r'model', ModelViewSet)


urlpatterns = [
	# path('auto/brand/', BrandViewSet.as_view({'get': 'list'})),
	# path('auto/brand/detail/<int:pk>', BrandViewSet.as_view({
	#	'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),
	# path('auto/brand/create/', BrandViewSet.as_view({'post': 'create'})),
	path('auto/', include(router.urls)),  # http://127.0.0.1:8000/api/auto/
]