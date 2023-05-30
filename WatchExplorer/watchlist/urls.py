from django.urls import path
from watchlist.views import home, watch_list, search_watch_data
app_name = 'watchlist'
urlpatterns = [
    path('', watch_list, name='watch_list'),
    path('search/', search_watch_data, name='search'),
]
