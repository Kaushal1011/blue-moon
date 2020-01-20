from django.urls import path

from home import views as home_view
from programming import views as programming_view
from . import views

urlpatterns = [
    path('', home_view.index, name='index'),
    path('../programming/', programming_view.index, name='Programming'),
    path('', views.index, name='Music'),
    path('', views.index, name='Design'),

]
