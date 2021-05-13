from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.services.forms import ServiceForm
from apps.services.models import Services, ServiceType
from apps.services.serializers import ServiceTypeSerializer, ServicesSerializer


class ServiceCreate(CreateView):
    model = Services
    form_class = ServiceForm
    template_name = 'services/service_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('order_services')


class ServiceTypeViewSet(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'website']


class ServiceViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    @action(detail=False, methods=['get'], url_path='result_sum', url_name='result_sum')
    def result_sum_services(self, request):
        params = request.query_params
        params_type = [int(i) for i in params.getlist('type[]')]
        params_count = int(params.get('count'))
        all_price = ServiceType.objects.filter(id__in=params_type).aggregate(all_price=Sum('price'))
        return Response(all_price.get('all_price') * params_count)
