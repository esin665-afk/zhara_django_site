from django.db import models

class BotUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

class BotOrder(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, db_column='user_id', to_field='telegram_id', null=True, blank=True)
    event_date = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Новый', blank=True, null=True)

    # Наши поля для заявок с сайта
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")

    class Meta:
        managed = False
        db_table = 'orders'
        ordering = ['-created_at']
