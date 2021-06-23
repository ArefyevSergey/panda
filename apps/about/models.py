from django.db import models


class Slider(models.Model):
    img = models.ImageField(upload_to='img/slider/', verbose_name='Картинка')
    alt = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class Contacts(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес')
    tel = models.CharField(max_length=15, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
