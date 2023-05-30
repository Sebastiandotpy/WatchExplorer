from django.shortcuts import render
from .models import WatchData

def home(request):
    saved_watch_data = WatchData.objects.all()
    context = {
        'saved_watch_data': saved_watch_data
    }
    return render(request, 'watchlist/home.html', context)

def search_watch_data(request):
    return render(request, 'watchlist/search.html')

def watch_list(request):
    saved_watch_data = WatchData.objects.all()
    context = {
        'saved_watch_data': saved_watch_data
    }
    return render(request, 'watch-list.html', context)
