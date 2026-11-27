from django.contrib import admin
from .models import Genre, Song


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'genre', 'price', 'display_duration', 'is_active')
    list_filter = ('genre', 'is_active')
    search_fields = ('title', 'artist')
    list_editable = ('price', 'is_active')

    def display_duration(self, obj):
        minutes = int(obj.duration)
        seconds = int((obj.duration - minutes) * 60)
        if seconds > 0:
            return f"{minutes}:{seconds:02d} мин"
        return f"{minutes} мин"

    display_duration.short_description = "Длительность"
