from django.urls import path

from . import views

app_name = 'history'
urlpatterns = [
    # path for artists
    path('', views.index, name='index'),
    # path for artist detail
    path('<int:artist_id>/', views.detail, name='detail'),

    path('songs/add/', views.add_song_form, name='add_song_form'),
    path('songs/post/', views.post_song, name='post_song'),

    path('artists/add', views.add_artist_form, name='add_artist_form'),
    path('artists/post', views.post_artist, name='post_artist'),

    path('songs/<int:song_id>/', views.song_detail, name='song_detail'),
]