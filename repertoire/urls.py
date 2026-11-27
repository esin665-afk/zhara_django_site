from django.urls import path
from . import views

urlpatterns = [
    path('', views.repertoire_list, name='repertoire'),
]
