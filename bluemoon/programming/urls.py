from django.urls import path, re_path

from home import views as home_view
from music import views as music_view
from . import views

urlpatterns = [
    path('', home_view.index, name='index'),
    path('', views.index, name='Programming'),
    path('../music/', music_view.index, name='Music'),
    re_path(r'(?P<title>[-a-zA-Z0-9_]+)/$',
            views.readmore, name="detail"),
    path('', views.index, name='Design'),

]
