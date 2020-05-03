from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='service-home'),
    path('about/', views.about, name='service-about'),
]