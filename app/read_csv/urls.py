from django.urls import path

urlpatterns = [
    path('<str:s>', app.read_csv.views.index, name='reader'),
]
