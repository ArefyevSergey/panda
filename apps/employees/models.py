from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    post = models.CharField(max_length=256, verbose_name='Должность')
    photo = models.ImageField(upload_to='img/employees/%Y/%m/%d', verbose_name='Фото')
    relevance = models.IntegerField(
        verbose_name='Релевантность',
        help_text='Последовательность в каком порядке будут выводится на странице "Команда"')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.name}, {self.post}'
