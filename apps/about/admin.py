from django.contrib import admin

from apps.about.models import Slider, Contacts


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass
