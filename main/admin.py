from django.contrib import admin
from .models import BotOrder

@admin.register(BotOrder)
class BotOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'event_date', 'created_at', 'status')
    search_fields = ('name', 'phone')
