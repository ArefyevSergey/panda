# Generated by Django 3.2 on 2021-06-06 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_specialists_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promocode',
            options={'verbose_name': 'Промо-код', 'verbose_name_plural': 'Промо-коды'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterModelOptions(
            name='servicetype',
            options={'verbose_name': 'Тип услуги', 'verbose_name_plural': 'Типы услуг'},
        ),
        migrations.AlterModelOptions(
            name='specialists',
            options={'verbose_name': 'Специалист', 'verbose_name_plural': 'Специалисты'},
        ),
        migrations.AlterModelOptions(
            name='website',
            options={'verbose_name': 'Сайт', 'verbose_name_plural': 'Сайты'},
        ),
    ]