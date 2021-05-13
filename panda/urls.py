from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('apps.about.urls')),
    path('account/', include('apps.accounts.urls')),
    path('employees/', include('apps.employees.urls')),
    path('frequently_asked_questions/', include('apps.frequently_asked_questions.urls')),
    path('services/', include('apps.services.urls')),
    path('', include('apps.main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
