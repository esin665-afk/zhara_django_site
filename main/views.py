import os
import requests
from django.shortcuts import render
from .models import BotOrder

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '')


def index(request):
    """Главная страница сайта."""
    return render(request, 'main/index.html')


def contacts(request):
    """Страница с контактами."""
    return render(request, 'main/contacts.html')


def booking(request):
    if request.method != 'POST':
        return render(request, 'main/booking.html')

    name = request.POST.get('name', '').strip()
    phone = request.POST.get('phone', '').strip()
    event_date = request.POST.get('event_date', '').strip()

    if not name or not phone:
        return render(request, 'main/booking.html', {'error': 'Укажите имя и телефон'})

    BotOrder.objects.create(
        name=name,
        phone=phone,
        event_date=event_date,
        status='Новый',
    )

    text = (
        f"🔥 Новая заявка с сайта!\n\n"
        f"👤 Имя: {name}\n"
        f"📞 Телефон: {phone}\n"
        f"📅 Дата: {event_date}"
    )

    try:
        response = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT_ID, "text": text},
            timeout=25,
        )
        if not response.ok:
            print(f"Telegram ответил ошибкой: {response.status_code} {response.text}")
        else:
            print("Уведомление отправлено")
    except Exception as e:
        print(f"Ошибка Telegram: {e}")

    return render(request, 'main/success.html')
