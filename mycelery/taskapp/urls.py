from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ReviewEmailView, alertView

urlpatterns = [
    path('', ReviewEmailView.as_view(), name='messenger'),
    path('alert/', alertView, name='alert')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
