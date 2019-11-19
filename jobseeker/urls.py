from django.urls import path
from . import views

urlpatterns = [
    path('jobseeker/', views.jobseeker, name = 'viahire-jobseeker'),
    path('postCV/', views.postCV, name = 'viahire-postCV'),
]
