from django.views.generic import TemplateView

from apps.about.models import Contacts, Slider


class MainView(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        context['contact'] = Contacts.objects.all()[0]
        return context
