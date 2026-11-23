from django.db import models


class BotUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.first_name or str(self.telegram_id)


class BotOrder(models.Model):
    STATUS_CHOICES = [
        ('Новый', 'Новый'),
        ('Подтвержден', 'Подтвержден'),
        ('Оплачен', 'Оплачен'),
        ('Отменен', 'Отменен'),
    ]

    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, db_column='user_id', null=True, blank=True)
    event_date = models.CharField(max_length=50, blank=True, null=True, verbose_name="Дата мероприятия")
    total_price = models.IntegerField(blank=True, null=True, verbose_name="Сумма, руб.")
    total_time = models.FloatField(blank=True, null=True, verbose_name="Длительность, мин.")
    created_at = models.DateTimeField(blank=True, null=True, verbose_name="Создан")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Новый', blank=True, null=True, verbose_name="Статус")

    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")

    class Meta:
        managed = False
        db_table = 'orders'
        ordering = ['-created_at']

    def __str__(self):
        return f"Заказ #{self.pk} — {self.name or '—'} ({self.event_date or '—'})"

    @property
    def total_minutes(self):
        return round(self.total_time or 0, 1)


class Song(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    duration = models.FloatField()

    class Meta:
        managed = False
        db_table = 'songs'
        ordering = ['title']

    def __str__(self):
        return self.title


class OrderSong(models.Model):
    order = models.ForeignKey(BotOrder, on_delete=models.CASCADE, db_column='order_id', related_name='order_songs')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, db_column='song_id')

    class Meta:
        managed = False
        db_table = 'order_songs'
        unique_together = ('order', 'song')

    def __str__(self):
        return f'{self.order_id} — {self.song.title if self.song else "—"}'
