from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from apps.services.views import ServiceCreate, ServiceTypeViewSet, ServiceViewSet

router = routers.SimpleRouter()

router.register(r'service-type', ServiceTypeViewSet, basename='service_type')
router.register(r'api', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
    path('', ServiceCreate.as_view(), name='order_services'),
]
