from django.shortcuts import render
from django.views.generic import ListView, DetailView
import datetime

from .models import Album, Artist, Song


# Create your views here.
class AlbumListView(ListView):
    model = Artist
    template_name = 'albums/album_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Artist.objects.order_by('name')


class AlbumDetailView(DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.object
        context["tracklist"] = album.song_set.all().order_by('no')
        total = datetime.timedelta(0, 0)
        for track in context['tracklist']:
            total += track.length
            track.length = str(track.length)[2:]
        context["total"] = total
        return context


class ArtistDetailView(DetailView):
    model = Artist
