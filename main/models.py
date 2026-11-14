from django.db import models

class Song(models.Model):
    """Модель для представления песни в базе данных."""
    title = models.CharField(max_length=255, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    duration = models.FloatField(verbose_name="Длительность (мин)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"
