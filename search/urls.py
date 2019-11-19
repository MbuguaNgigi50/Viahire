from django.urls import path
from .views import SortView

urlpatterns = [
    path('sortdetails/', SortView , name = 'sort'),
]
