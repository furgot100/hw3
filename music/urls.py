from django.urls import path

from . import views

app_name = 'music'
urlpatterns = [
  path('', views.home, name='home'),
  path('<int:musician_id>/', views.musician_detail, name='musician_detail'),
  path('album/<int:album_id>/', views.album_detail, name='album_detail'),
  path('song/<int:song_id>/', views.song_detail, name='song_detail'),
]