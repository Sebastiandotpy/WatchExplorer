from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('watchlist.urls')),  # Include the URLs from the watchlist app
]
