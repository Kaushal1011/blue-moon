from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('',views.index, name='Programming'),
    path('',views.index, name='Music'),
    path('',views.index, name='Design'),

]
