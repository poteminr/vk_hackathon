from .forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse
from . import models
from .forms import ReviewForm, LoginForm
from django.contrib.auth import views as auth_views


class CustomLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'



class RegisterView(generic.View):
    template = 'registration/registration.html'
    Form = CustomUserCreationForm

    def get(self, request):
        form = self.Form()

        return render(request, self.template, context = {"form": form})


    def post(self, request):
        filled_form = self.Form(request.POST)

        if filled_form.is_valid():
            filled_form.save()
            return redirect("index")

        return render(request, self.template, context = {"form": filled_form})

class DetailUser(generic.View):
    model = models.CustomUser
    template = "user/user_detail.html"

    def get(self, request, id):

        obj = get_object_or_404(self.model, id=id)
        context = {"object": obj}

        return render(request, self.template, context = context)

class ReviewCreate(generic.View):
    model = models.Review
    template = "user/review_create.html"
    Form = ReviewForm

    def get(self, request, id):
        obj = self.model.objects.get(id=id)
        
        form = self.Form()

        return render(request, self.template, context = {"form" : form, "obj":obj})

    def post(self, request, id):
        obj = self.model.objects.get(id=id)
        
        filled_form = self.Form(
                                request.POST, 
                                author=request.user,
                                rew_user=obj,
                        )
        if filled_form.is_valid():
            upd_instance = filled_form.save()

            return redirect(obj)
        return render(request, self.template, context = {"form" : filled_form, "obj":obj})


