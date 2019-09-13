from django.urls import path, include, re_path
# from django.views.generic import ListView, DetailView 
from .models import *
from users import views
from users.forms import LoginForm


urlpatterns = [     
    path('<int:id>/update', views.UpdateView.as_view(), name='user_update'),
    path('', include('django.contrib.auth.urls')),
    path('login', views.CustomLoginView.as_view() , name='login'),
    
    path('<int:id>', views.DetailUser.as_view(), name='user_detail'),
    path('<int:id>/create_review', views.ReviewCreate.as_view(), name='user_review')
]
