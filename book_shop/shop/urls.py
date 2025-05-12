from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('book_form/', views.book_register, name='book_register'),
    path('book_stock', views.book_stock, name='book_stock'),
    path('register/', views.register_student, name='register_student'),
]
