from django.shortcuts import render
from .models import WatchData, Category

def home(request):
    saved_watch_data = WatchData.objects.all()
    watch_categories = Category.objects.all()
    context = {
        'saved_watch_data': saved_watch_data,
        'watch_categories': watch_categories
    }
    return render(request, 'watchlist/home.html', context)


def search_watch_data(request):
    # Handle the search logic here
    query = request.GET.get('query')
    # Perform the search operation based on the query
    search_results = WatchData.objects.filter(title__icontains=query)
    context = {
        'query': query,
        'search_results': search_results
    }
    return render(request, 'watchlist/search_results.html', context)


def watch_list(request):
    # Handle the watch list logic here
    watch_list_data = WatchData.objects.filter(user_name=request.user)
    context = {
        'watch_list_data': watch_list_data
    }
    return render(request, 'watchlist/watch_list.html', context)
