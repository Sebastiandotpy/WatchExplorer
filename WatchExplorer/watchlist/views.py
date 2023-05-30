from django.shortcuts import render
from .models import WatchData


def home(request):  # http://127.0.0.1:8000/
    saved_watch_data = WatchData.objects.all()
    context = {
        'saved_watch_data': saved_watch_data
    }
    return render(request, 'watchlist/home.html', context)


def search_watch_data(request):     # http://127.0.0.1:8000/watchlist/search/
    return render(request, 'watchlist/search.html')


def watch_list(request):    # http://127.0.0.1:8000/watchlist/
    saved_watch_data = WatchData.objects.all()
    context = {
        'saved_watch_data': saved_watch_data
    }
    return render(request, 'watchlist/watch-list.html', context)
