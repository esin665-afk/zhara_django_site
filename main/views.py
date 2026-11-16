from django.shortcuts import render
from .models import BotOrder
import requests

# --- НАСТРОЙКИ ТЕЛЕГРАМ БОТА ---
TELEGRAM_BOT_TOKEN = "8767475737:AAEH-wPt2Xred_XaDzcyLp69A8DxT-G7g60"
TELEGRAM_CHAT_ID = 1606744507

def index(request):
    """Главная страница сайта."""
    return render(request, 'main/index.html')

def contacts(request):
    """Страница с контактами."""
    return render(request, 'main/contacts.html')

def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        event_date = request.POST.get('event_date')

        # 1. Сначала сохраняем заявку в базу данных (общая таблица orders)
        BotOrder.objects.create(
            name=name,
            phone=phone,
            event_date=event_date,
            status='Новый'
        )

        # 2. ОТПРАВЛЯЕМ УВЕДОМЛЕНИЕ В TELEGRAM
        text = f"🔥 Новая заявка с сайта!\n\n👤 Имя: {name}\n📞 Телефон: {phone}\n📅 Дата: {event_date}"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

        try:
            # Отправляем запрос (таймаут 5 сек, чтобы страница не висела, если TG недоступен)
            requests.post(url, json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": text,
                "parse_mode": "HTML"
            }, timeout=5)
        except Exception as e:
            print(f"Ошибка Telegram: {e}")

        # 3. ТОЛЬКО ТЕПЕРЬ ВЫВОДИМ ОТВЕТ НА САЙТЕ (возвращаем красивую страницу)
        return render(request, 'main/success.html')

    # Если это GET-запрос (пользователь просто зашел на страницу), показываем форму
    return render(request, 'main/booking.html')
