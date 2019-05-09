# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add',views.add,name='add'),
    path('video',views.video,name='video'),
    path('analys/<int:num>', views.analys, name='analys'),
    path('find', views.find, name='find'),
]