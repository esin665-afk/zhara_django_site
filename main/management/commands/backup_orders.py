from django.core.management.base import BaseCommand
from django.core.management import call_command
from datetime import datetime

class Command(BaseCommand):
    help = 'Создает резервную копию всех заказов (BotOrder) в формате JSON'

    def handle(self, *args, **kwargs):
        # Получаем текущую дату и время для названия файла
        now = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"orders_backup_{now}.json"

        self.stdout.write(self.style.NOTICE(f'📦 Создаем бэкап заказов в файл {filename}...'))

        try:
            # Вызываем стандартную команду dumpdata
            call_command('dumpdata', 'main.BotOrder', '--indent', '4', '--output', filename)
            self.stdout.write(self.style.SUCCESS(f'✅ Бэкап успешно создан: {filename}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Ошибка при создании бэкапа: {e}'))
