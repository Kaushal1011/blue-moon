from django.urls import path

from . import views
from music import views as music_views
from programming import views as programming_views
urlpatterns = [
    path('', views.index, name='index'),
    path('programming/', programming_views.index, name='Programming'),
    path('music/', music_views.index, name='Music'),
    path('', views.index, name='Design'),

]
