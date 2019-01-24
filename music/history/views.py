from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Artist
from .models import Song

# Create your views here.
def index(request):
    artist_list = Artist.objects.all()
    context = {'artist_list': artist_list}
    return render(request, 'history/index.html', context)

def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    artist_songs = Song.objects.filter(artist_id=artist_id)
    context = {'artist': artist, 'songs': artist_songs}
    print(context)
    return render(request, 'history/detail.html', context)

def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    # in the process of creating a song detail page where the artist is clickable
    # song_artist = Artist.objects.filter(song.artist_id=artist)
    context = {'song': song}
    return render(request, 'history/songs/song_detail.html', context)


def add_song_form(request):
    artist_list = Artist.objects.all()
    context = {'artist_list': artist_list}
    return render(request, 'history/add_song.html', context)


def post_song(request):
    song = request.POST["song_title"]
    artist = request.POST["selected_artist"]
    new_song = Song(song_title=song ,artist_id=artist)
    new_song.save()
    return HttpResponseRedirect(reverse('history:index'))

def add_artist_form(request):
    return render(request, 'history/add_artist.html')

def post_artist(request):
    artist = request.POST["artist_name"]
    new_artist = Artist(artist_name=artist)
    new_artist.save()
    return HttpResponseRedirect(reverse('history:index'))

