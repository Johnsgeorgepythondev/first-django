from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('forms.urls')),
    path('home/', views.register_student),
]