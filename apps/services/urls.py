from django.conf.urls import include
from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers

from apps.services.views import ServiceCreate, ServiceTypeViewSet, ServiceViewSet

router = routers.SimpleRouter()

router.register(r'service-type', ServiceTypeViewSet, basename='service_type')
router.register(r'api', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
    path('', ServiceCreate.as_view(), name='order_services'),
    # path('', TemplateView.as_view(template_name='services/services.html'), name='services'),
]
