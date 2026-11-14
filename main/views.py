from django.shortcuts import render
from django.http import HttpResponse # Импортируем HttpResponse

def index(request):
    """Главная страница сайта."""
    return render(request, 'main/index.html')  # <-- Обновили путь

def contacts(request):
    """Страница с контактами."""
    return render(request, 'main/contacts.html')  # <-- Обновили путь


def booking(request):
    """Страница бронирования с обработкой POST-запроса."""
    if request.method == 'POST':
        # Ловим данные из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        event_date = request.POST.get('event_date')

        # Выводим в консоль для проверки (потом заменим на сохранение в БД)
        print(f"Новая заявка! Имя: {name}, Тел: {phone}, Дата: {event_date}")

        return HttpResponse(f"Спасибо, {name}! Ваша заявка на {event_date} принята.")

    # Если это GET-запрос, просто показываем форму
    return render(request, 'main/booking.html')
