# Generated by Django 3.2 on 2021-06-05 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frequently_asked_questions', '0002_faq_relevance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'Вопрос Ответ', 'verbose_name_plural': 'Вопросы Ответы'},
        ),
    ]
