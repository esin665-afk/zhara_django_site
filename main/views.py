from django.shortcuts import render
from django.http import HttpResponse
from .models import BookingRequest  # <-- ВАЖНО: Импортируем нашу модель

def index(request):
    """Главная страница сайта."""
    return render(request, 'main/index.html')

def contacts(request):
    """Страница с контактами."""
    return render(request, 'main/contacts.html')

def booking(request):
    """Страница бронирования с сохранением в БД."""
    if request.method == 'POST':
        # Ловим данные из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        event_date = request.POST.get('event_date')

        # СОХРАНЯЕМ В БАЗУ ДАННЫХ (вместо print)
        BookingRequest.objects.create(
            name=name,
            phone=phone,
            event_date=event_date
        )

        # Возвращаем страницу "Спасибо" (текстом)
        return HttpResponse(f"<h1 style='color: green;'>Спасибо, {name}!</h1><p>Ваша заявка на {event_date} сохранена в базе.</p><a href='/'>Вернуться на главную</a>")

    # Если это GET-запрос, просто показываем форму
    return render(request, 'main/booking.html')
