from django.urls import path
from . import views

app_name = 'repertoire'

urlpatterns = [
    path('', views.repertoire_list, name='list'),
]
