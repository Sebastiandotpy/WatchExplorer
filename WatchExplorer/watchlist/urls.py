from django.urls import path
from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_watch_data, name='search'),
    path('watch-list/', views.watch_list, name='watch-list'),
]
