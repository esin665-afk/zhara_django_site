from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем маршруты из приложения main, используя пространство имен 'main'
    path('', include('main.urls', namespace='main')),
]
