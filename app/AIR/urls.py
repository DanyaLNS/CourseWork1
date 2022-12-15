from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('read_csv/', include('read_csv.urls')),
    path('api/', include('api.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
