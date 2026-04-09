from django.shortcuts import render
from .models import Song, Artist

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music/artist_list.html', {'artists': artists})