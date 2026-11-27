from django.db import models

# Create your models here.
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Жанр")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ['name']


class Song(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название песни")
    artist = models.CharField(max_length=200, verbose_name="Исполнитель", blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='songs', verbose_name="Жанр")
    duration = models.FloatField(help_text="Длительность в минутах", verbose_name="Длительность (мин)") # <-- ИЗМЕНИЛИ ТИП
    price = models.IntegerField(default=3000, verbose_name="Цена, руб.")
    is_active = models.BooleanField(default=True, verbose_name="В репертуаре")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"
        ordering = ['genre', 'title']
