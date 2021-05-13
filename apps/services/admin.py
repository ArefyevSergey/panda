from django.contrib import admin

from apps.services.models import PromoCode, Specialists, Website, ServiceType, Services


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialists)
class SpecialistsAdmin(admin.ModelAdmin):
    pass


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    pass
