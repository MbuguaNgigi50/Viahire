from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'viahire-home'),
    path('about/', views.about, name = 'viahire-about'),
]
