from django.urls import path
from . import views
from .views import *


urlpatterns = [
  
    path('login/',views.login,name="login"),
    path('',views.home, name='home'),
    path('calculatetransport/',views.calculatetransport),
    path('calculate/',views.calculate),
    path('request/',views.request, name='request'),
    #path('login/',views.login),
    path('calculatehouse/',views.calculatehouse),
    path('option/',views.option, name='option'),
    path('monitor/',views.monitor),
    path('reduces/',views.reduces, name='reduces'),
    path('individual/',views.individual, name='individual'),
    path('organisation/',views.organisation, name='organisation'),
    path('leaderboard/',views.leaderboard),
    path('howitworks/',views.howitworks, name='howitworks'),
    path('organisationreduces/',views.organisationreduces, name='organisationreduces'),
]   


