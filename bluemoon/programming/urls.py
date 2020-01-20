from django.urls import path

from home import views as home_view
from music import views as music_view
from . import views

urlpatterns = [
    path('', home_view.index, name='index'),
    path('', views.index, name='Programming'),
    path('../music/', music_view.index, name='Music'),
    path('', views.index, name='Design'),

]
