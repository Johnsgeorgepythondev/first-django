from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signup, name='signup'),  
    path("signin/", views.signin, name='signin'),
    path('signout/', views.signout, name='signout'), 
    path("about/", views.about, name='about'),
    path("payment/",views.payment,name='payment'),
    path("cart/<int:product_id>/", views.cart, name='cart'),
    path("", views.home, name="home"),
    path('<slug:slug_c>/', views.home, name='product_by_category'),
    path('<slug:slug_c>/<slug:slug_p>/', views.product_detail, name='product_detail'),
]
