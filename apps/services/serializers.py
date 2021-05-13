from rest_framework import serializers

from apps.services.models import ServiceType, Services


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id', 'name', 'website', 'price']


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'website', 'type', 'specialist', 'count']
