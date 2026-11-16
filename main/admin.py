from django.contrib import admin
from .models import BookingRequest

@admin.register(BookingRequest)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'event_date', 'created_at')
    search_fields = ('name', 'phone')
