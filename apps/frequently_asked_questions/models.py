from django.db import models


class FAQ(models.Model):
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')
    relevance = models.IntegerField(
        verbose_name='Релевантность',
        help_text='Последовательность в каком порядке будут выводится на странице "F.A.Q"'
    )

    class Meta:
        verbose_name = 'Вопрос Ответ'
        verbose_name_plural = 'Вопросы Ответы'
