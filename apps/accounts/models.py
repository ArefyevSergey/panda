from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    GENDER_CHOICES = (
        ('F', 'Мужской',),
        ('M', 'Женский',),
        ('U', 'Не выбрано',),
    )
    user = models.OneToOneField(User, blank=True, default=None, on_delete=models.SET_DEFAULT)
    fio = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    consent_processing_personal_data = models.BooleanField(verbose_name='Согласие на обработку персональных данных',
                                                           default=True)

    def __str__(self):
        return self.user.username or self.fio

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
