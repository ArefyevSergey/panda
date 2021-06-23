from django.views.generic.list import ListView

from apps.about.models import Contacts
from apps.frequently_asked_questions.models import FAQ


class FAQListView(ListView):
    model = FAQ
    template_name = 'frequently_asked_questions/frequently_asked_questions.html'
    ordering = 'relevance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contacts.objects.all()[0]
        return context
