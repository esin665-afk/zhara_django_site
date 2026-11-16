from django.db import models

class BookingRequest(models.Model):
    """Модель для заявок на выступление с сайта"""
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    event_date = models.DateField(verbose_name="Дата мероприятия")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заявки")

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        verbose_name = "Заявка на выступление"
        verbose_name_plural = "Заявки на выступление"
