from django import forms
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.db.models import F, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.base import View
from django.views.generic.edit import FormView

from .forms import LoginForm, ProfileForm, EmailChangeForm
from ..services.models import Services, PromoCode


class RegisterFormView(FormView):
    form_class = ProfileForm
    success_url = "/account/login/"
    template_name = "accounts/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    success_url = "/"

    def form_valid(self, form):
        user = form.get_user()
        if user:
            login(self.request, user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class ProfileView(DetailView):
    model = User
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.filter(user=self.request.user).annotate(sum=Sum('type__price') * F('count'))
        context['promo_codes'] = PromoCode.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'password-change' in request.POST:
            return self._password_change(request)
        if 'email-change' in request.POST:
            return self._email_change(request)
        return self.render_to_response(self.get_context_data())

    def _password_change(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile', user.id)
        return self.render_to_response(self.get_context_data(password_change_form=form))

    def _email_change(self, request):
        form = EmailChangeForm(request.POST)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()
            return redirect('profile', request.user.id)
        return self.render_to_response(self.get_context_data(email_change_form=form))
