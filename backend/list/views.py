from django.shortcuts import render
from list import models
# Create your views here.

def render_hw(request):

    return render(request, "index.html", context={
        "text": "Hello",
    })

def posts_list(request):

    return render(request, "list_view.html", context={
        "posts": models.Post.objects.all() ,
    })