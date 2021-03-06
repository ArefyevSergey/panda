# Generated by Django 3.2 on 2021-05-13 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('F', 'Мужской'), ('M', 'Женский'), ('U', 'Не выбрано')], max_length=1)),
                ('user', models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
