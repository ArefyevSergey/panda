import re

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.db import transaction
from django.forms.utils import ErrorList

from apps.accounts.models import Profile
from apps.services.models import PromoCode


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    user_cache = None

    error_messages = {
        'not_found': u"Неправильный логин",
        'invalid_password': "Неправильный пароль",
        'inactive': "This account is inactive.",
        'ascii_error': u"В пароле не должно быть русских символов",
    }

    def get_user(self):
        return self.user_cache

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(
                username=username,
                password=password
            )

            if not User.objects.filter(username=username):
                self._errors["username"] = ErrorList([
                    self.error_messages['not_found']
                ])
            if self.user_cache is None:
                self._errors["password"] = ErrorList([
                    self.error_messages['invalid_password']
                ])
        return self.cleaned_data


class ProfileForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    error_messages = {
        'not_validation_username_pattern': 'Логин должен иметь длинну от 3 до 64 символов и содержать только '
                                           'символы (a-z, а-я, 1-0, @, !, ^, _)',
        'not_validation_password_pattern': 'Пароль должен иметь длинну от 6 до 64 символов и содержать только '
                                           'символы (a-z, 1-0, @, !, ^, _)',
        'not_validation_fio_pattern': 'ФИО должно иметь длинну от 6 до 64 символов, иметь формат '
                                      '"ФАМИЛИЯ ИМЯ ОТЧЕСТВО" и содержать только символы (a-z, а-я, A-Z, А-Я)',
        'not_validation_phone_number_pattern': 'Телефоный номер должен иметь формат "+71234567890"',
        'not_validation_gender_pattern': 'Указан неизвестный пол',
        'username_already_exists': 'Пользователь с таким логином уже зарегистрирован',
    }

    class Meta:
        model = Profile
        fields = ('username', 'password', 'fio', 'phone_number', 'gender')

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            self._errors["username"] = ErrorList([
                self.error_messages['username_already_exists']
            ])

        pattern = r'^[a-zа-я0-9!@^_]{3,64}$'
        if not re.fullmatch(pattern, username):
            self._errors["username"] = ErrorList([
                self.error_messages['not_validation_username_pattern']
            ])
        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        pattern = r'^[a-z0-9!@^_]{5,64}$'
        if not re.fullmatch(pattern, password):
            self._errors["password"] = ErrorList([
                self.error_messages['not_validation_password_pattern']
            ])
        return password

    def clean_fio(self):
        fio = self.cleaned_data['fio']

        pattern = r'^[a-zа-яA-ZА-Я]{1,}\s[a-zа-яA-ZА-Я]{1,}\s[a-zа-яA-ZА-Я]{1,}$'
        if not re.fullmatch(pattern, fio):
            self._errors["fio"] = ErrorList([
                self.error_messages['not_validation_fio_pattern']
            ])
        return fio

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        pattern = r'^[+][0-9]{10,16}$'
        if not re.fullmatch(pattern, phone_number):
            self._errors["phone_number"] = ErrorList([
                self.error_messages['not_validation_phone_number_pattern']
            ])
        return phone_number

    def clean_gender(self):
        gender = self.cleaned_data['gender']

        pattern = '^[MFU]{1}$'
        if not re.fullmatch(pattern, gender):
            self._errors["gender"] = ErrorList([
                self.error_messages['not_validation_gender_pattern']
            ])
        return gender

    @transaction.atomic
    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password"]
        )
        profile = super().save(commit=False)
        profile.user = user
        if commit:
            profile.save()
            self._create_promo_code(user)
        return profile

    def _create_promo_code(self, user):
        PromoCode.objects.get_or_create(code=get_random_string(length=10), user=user)


class EmailChangeForm(forms.Form):
    email = forms.EmailField(required=True)
