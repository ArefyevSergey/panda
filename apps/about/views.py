from django.views.generic import TemplateView

from apps.about.models import Contacts


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contacts.objects.all()[0]
        return context
