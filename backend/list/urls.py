from django.urls import path
from django.shortcuts import render, redirect
from list import views

urlpatterns = [
    path('', views.posts_list),
]