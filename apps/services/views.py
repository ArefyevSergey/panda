from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.about.models import Contacts
from apps.services.forms import ServiceForm
from apps.services.models import Services, ServiceType
from apps.services.serializers import ServiceTypeSerializer, ServicesSerializer


class ServiceCreate(CreateView):
    model = Services
    form_class = ServiceForm
    template_name = 'services/service_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contacts.objects.all()[0]
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        form.save_m2m()
        # self._send_email_specialist(self.object)
        return HttpResponseRedirect(self.get_success_url())

    def _send_email_specialist(self, services: Services):
        subject = f'Заказ услуги'
        message = f'Заказана услуга от {services.user.profile.fio}.\n\n' \
                  f'Заказ для сайта {services.website.name} по услугам {", ".join(services.type.all().values_list("name", flat=True))}\n' \
                  f'На общую сумму {self._result_sum(services)} ₽'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [services.specialist.email], fail_silently=False)

    def _result_sum(self, services: Services):
        count_services = services.count
        all_price = services.type.all().aggregate(all_price=Sum('price'))
        return round(all_price.get('all_price') * count_services, 2)

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
