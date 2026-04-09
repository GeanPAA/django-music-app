from django.contrib import admin
from django.urls import path
from music.views import song_list, artist_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('songs/', song_list),
    path('artists/', artist_list),
]