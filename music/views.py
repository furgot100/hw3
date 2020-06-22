from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Musician, Song

# Create your views here.
def home(request):
    context = {
        'artists' : Musician.objects.all()
    }
    return render(request, 'home.html', context)

def musician_detail(request, musician_id):
    context = {
        'albums': Album.objects.all(),
        'artist' : Musician.objects.get(id=musician_id),
    }
    return render(request,'musician/detail.html',context)

def album_detail(request, album_id):
    context= {
        'songs': Song.objects.all(),
        'album' : Album.objects.get(id=album_id),
    }

    return render(request, 'album/detail.html', context)
def song_detail(request, song_id):
    context={
        'song' : Song.objects.get(id=song_id),
    }

    return render(request, 'song/detail.html',context)