from django.contrib import admin

from apps.frequently_asked_questions.models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass
