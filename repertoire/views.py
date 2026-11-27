from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Genre, Song


def repertoire_list(request):
    genres = Genre.objects.all()
    songs = Song.objects.filter(is_active=True).select_related('genre')

    # Фильтр по жанру, если передан параметр
    genre_slug = request.GET.get('genre')
    if genre_slug:
        songs = songs.filter(genre__slug=genre_slug)

    return render(request, 'repertoire/repertoire.html', {
        'genres': genres,
        'songs': songs,
        'current_genre': genre_slug,
    })
