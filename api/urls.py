from django.urls import path
from . import views
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [
    path('<str:s>', views.ReaderView.as_view(), name='reader'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
