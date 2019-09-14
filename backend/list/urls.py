from django.urls import path
from django.shortcuts import render, redirect
from list import views

urlpatterns = [
    path('', views.posts_list, name="post_list"),
    path('ml', views.posts_clever_list, name="post_list_cleaver"),
    path('<str:slug>/', views.post_detail, name='post_detail'),
    path('create', views.PostCreateForm.as_view(), name="post_create"),
    path('order/<str:slug>/delete', views.post_delete, name='post_delete'),
]