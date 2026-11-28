from django.core.management.base import BaseCommand
from django.core.management import call_command
from repertoire.models import Song, Genre

class Command(BaseCommand):
    help = 'Очищает репертуар и загружает песни из фикстуры repertoire_fixture.json'

    def handle(self, *args, **kwargs):
        # 1. Очищаем старые данные
        self.stdout.write(self.style.WARNING('🧹 Очищаем старый репертуар...'))
        Song.objects.all().delete()
        Genre.objects.all().delete()

        # 2. Загружаем фикстуру
        self.stdout.write(self.style.NOTICE('📥 Загружаем данные из фикстуры...'))
        try:
            call_command('loaddata', 'repertoire_fixture.json')
            self.stdout.write(self.style.SUCCESS('✅ Репертуар успешно обновлен!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Ошибка при загрузке: {e}'))
