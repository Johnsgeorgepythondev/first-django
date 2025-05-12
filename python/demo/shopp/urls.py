from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug_c>/',views.home,name="product_by_category"),
    path('contact/', views.contact, name='contact')

]

