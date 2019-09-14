from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

from ML.get_metrics import calc_metrics
from ML.text_prep import text_preproc
import numpy as np


def metrics_res(profile_info, ivent):
    profile_info = [text_preproc(data) for data in profile_info]
    ivent = text_preproc(ivent)
    
    metric = calc_metrics(profile_info, ivent)
    
    return metric

from list import models, forms
# Create your views here.

def render_hw(request):

    return render(request, "index.html", context={
        "text": "Hello",
    })

def posts_list(request):

    return render(request, "list_view.html", context={
        "posts": models.Post.objects.all() ,
    })
def posts_clever_list(request):

    user = request.user

    if user.is_anonymous:
        return redirect("/") 

    def sort_function(post):

        profile_info = [user.name, user.additionalinfo]

        post_add = post.title

        return metrics_res(profile_info, post_add)

    return render(request, "list_view.html", context={
        "posts": sorted(models.Post.objects.all(), key=sort_function, reverse=True),
    })

def post_detail(request, slug):
    template = "post_detail.html"
    obj = get_object_or_404(models.Post, slug__iexact = slug)
    context = {
            "object": obj,
            "have_access":obj.have_access(request.user, raise_403=False)
            }

    return render(request, template, context = context)

class PostCreateForm(LoginRequiredMixin, generic.View):
    template = "post_create.html"
    Form = forms.PostForm

    def get(self, request):
        form = self.Form()

        return render(request, self.template, context = {
            "form": form,
            })


    def post(self, request):
        
        filled_form = self.Form(request.POST, request.FILES, user=request.user)

        # photo = request.FILES.get("image", False)
        # if photo:
        #     filled_form.data["image"]=[photo.name]
        # print(filled_form.data)

        

        if filled_form.is_valid():
            inst = filled_form.save()

            # import pdb; pdb.set_trace();

            return redirect(reverse("post_list"))#redirect(inst)

        return render(request, self.template, context = {
            "form": filled_form,
            })
def post_delete(request, slug):
    obj = get_object_or_404(models.Post, slug__iexact=slug)
    obj.have_access(request.user)
    obj.delete()

    return redirect( reverse("post_list") )