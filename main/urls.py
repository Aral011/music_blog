
from django.contrib import admin
from django.urls import path
from music.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', get_hello),
    path('music/', get_music),
    path('music/<int:id>', get_song),
    path('music/create/', post_music)
]
