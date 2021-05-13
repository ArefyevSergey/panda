from django.contrib.auth.models import User
from django.db import models


class Specialists(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    post = models.CharField(max_length=256, verbose_name='Должность')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class PromoCode(models.Model):
    code = models.CharField(unique=True, max_length=255, verbose_name='Код')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.code


class Website(models.Model):
    code = models.CharField(unique=True, max_length=255, verbose_name='Код',
                            help_text='Уникальный код вебсайта. Например "vk"')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ServiceType(models.Model):
    name = models.CharField(max_length=255)
    website = models.ForeignKey(Website, on_delete=models.PROTECT, verbose_name='Вебсайт')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена',
                                help_text='Стоимость одной единицы')

    def __str__(self):
        return self.name


class Services(models.Model):
    website = models.ForeignKey(Website, on_delete=models.PROTECT, verbose_name='Вебсайт')
    type = models.ManyToManyField(ServiceType, verbose_name='Тип услуги')
    specialist = models.ForeignKey(Specialists, on_delete=models.PROTECT, verbose_name='Специалист')
    count = models.IntegerField(verbose_name='Количество услуг')
    promo_code = models.CharField(max_length=100, blank=False, verbose_name='Промо-код')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
