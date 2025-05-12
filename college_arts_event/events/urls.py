# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('create_event/', views.create_event, name='create_event'),
    path('participate/<int:event_id>/', views.participate, name='participate'),
    path('submit_result/', views.submit_result, name='submit_result'),
]
