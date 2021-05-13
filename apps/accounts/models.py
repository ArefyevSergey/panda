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

    def __str__(self):
        return self.user.username or self.fio
