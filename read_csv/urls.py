from django.urls import path

import read_csv.views


urlpatterns = [
    path('<str:s>', read_csv.views.index, name='reader'),
]
