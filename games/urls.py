
from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.games_list, name='list'),
    path('upload/', views.upload_game, name='upload'),
    path('<slug:slug>/', views.game_detail, name='detail'),
]
