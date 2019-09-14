from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse
from . import models
from .forms import ReviewForm, LoginForm
from django.contrib.auth import views as auth_views
from django.core.exceptions import PermissionDenied


class CustomLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'



class UpdateView(generic.View):
    template = 'user/update.html'
    Form = CustomUserChangeForm
    Model = models.CustomUser

    def get(self, request, id):
        obj = get_object_or_404(models.CustomUser, id=id)
        if request.user != obj:
            PermissionDenied()
        
        filled_form = self.Form(instance=obj)

        return render(request, self.template, context = {"form" : filled_form, "obj" : obj})

    def post(self, request, id):
        obj = get_object_or_404(models.CustomUser, id=id)
        
        if request.user != obj:
            PermissionDenied()


        updated_form = self.Form(request.POST, instance=obj)
        if updated_form.is_valid():
            upd_instance = updated_form.save()

            return redirect(upd_instance)
        return render(request, self.template, context = {"form" : updated_form, "obj" : obj})

class DetailUser(generic.View):
    model = models.CustomUser
    template = "user/user_detail.html"

    def get(self, request, id):

        obj = get_object_or_404(self.model, id=id)
        context = {"object": obj, "user_color": obj.get_color()}

        return render(request, self.template, context = context)

class ReviewCreate(generic.View):
    model = models.Review
    template = "user/review_create.html"
    Form = ReviewForm

    def get(self, request, id):
        obj = get_object_or_404(models.CustomUser, id=id)
        
        form = self.Form()

        return render(request, self.template, context = {"form" : form, "obj":obj})

    def post(self, request, id):
        obj = get_object_or_404(models.CustomUser, id=id)
        
        filled_form = self.Form(
                                request.POST, 
                                author=request.user,
                                rew_user=obj,
                        )

        if filled_form.is_valid():
            upd_instance = filled_form.save()

            return redirect(obj)
        return render(request, self.template, context = {"form" : filled_form, "obj":obj})


