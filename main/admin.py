from django.contrib import admin
from .models import BotOrder, BotUser, Song, OrderSong


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'duration')
    search_fields = ('title',)
    ordering = ('title',)

    def has_delete_permission(self, request, obj=None):
        return False


class OrderSongInline(admin.TabularInline):
    model = OrderSong
    extra = 0
    autocomplete_fields = ('song',)


@admin.register(BotOrder)
class BotOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_name', 'display_phone', 'event_date', 'total_price', 'total_minutes', 'status', 'created_at')
    list_display_links = ('id', 'display_name')
    list_select_related = ('user',)
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone', 'user__first_name', 'user__phone')
    date_hierarchy = 'created_at'
    list_per_page = 50
    list_editable = ('status',)
    readonly_fields = ('created_at',)
    inlines = [OrderSongInline]

    @admin.display(description='Имя')
    def display_name(self, obj):
        return obj.name or (obj.user.first_name if obj.user else '—')

    @admin.display(description='Телефон')
    def display_phone(self, obj):
        return obj.phone or (obj.user.phone if obj.user else '—')

    @admin.display(description='Длительность, мин.')
    def total_minutes(self, obj):
        return round(obj.total_time or 0, 1)


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'telegram_id', 'first_name', 'username', 'phone', 'created_at')
    search_fields = ('telegram_id', 'first_name', 'username', 'phone')
