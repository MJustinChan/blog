from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('edit/action/',views.edit_action,name='edit_action'),
    re_path(r'^edit/(?P<article_id>[0-9]+)$',views.edit_page,name='edit_page'),
    re_path(r'^article/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),
    path('c/', views.c),
    path('a/', views.a),
    path('b/', views.index),
]