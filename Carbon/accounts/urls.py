from django.urls import path
from . import views
from .views import *


urlpatterns = [
  
    path('login/',views.login,name="login"),
    path('',views.home),
    path('calculatetransport/',views.calculatetransport),
    path('calculate/',views.calculate),
    path('request/',views.request),
    #path('login/',views.login),
    path('calculatehouse/',views.calculatehouse),
    path('option/',views.option),
    path('monitor/',views.monitor),
    path('reduces/',views.reduces),
    path('individual/',views.individual),
    path('organisation/',views.organisation),
    path('leaderboard/',views.leaderboard),
    path('howitworks/',views.howitworks),
]   


