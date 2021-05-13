from django import forms
from django.forms.utils import ErrorList

from apps.services.models import Services, PromoCode


class ServiceForm(forms.ModelForm):
    promo_code = forms.CharField(max_length=100, required=False)

    error_messages = {
        'not_prom_code': 'Нет такого промо-кода',
    }

    class Meta:
        model = Services
        fields = ('website', 'type', 'specialist', 'count', 'promo_code',)

    def clean_promo_code(self):
        promo_code = self.cleaned_data['promo_code']

        if promo_code and promo_code not in PromoCode.objects.values_list('code', flat=True).all():
            self._errors["promo_code"] = ErrorList([
                self.error_messages['not_prom_code']
            ])

        return promo_code
