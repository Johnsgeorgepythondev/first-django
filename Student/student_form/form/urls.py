from django.urls import path, include
from . import views

urlpatterns = [

    path("", include('form.urls')),
    path("", views.index),
]
