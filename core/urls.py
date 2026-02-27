from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('welcome/', views.welcome, name='welcome'),
    path('game/', views.game, name='game'),
    path('special/', views.special, name='special'),
    path('letter/', views.letter, name='letter'),
    path('final/', views.final, name='final'),
]