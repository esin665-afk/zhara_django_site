from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('booking/', views.booking, name='booking'), # <-- НОВЫЙ МАРШРУТ
]
