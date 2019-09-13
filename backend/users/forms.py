from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Review
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'uk-input', 'placeholder' : ""}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'uk-input', 'placeholder' : ""}))

    


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser

        fields = UserCreationForm.Meta.fields + (
                "name",
                "email",
                "additionalinfo",
                "verified",
                "photo",
                )
        
        

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser

        fields = UserCreationForm.Meta.fields + (
                "name",
                "additionalinfo",
                "verified",
                "photo"
                )

class ReviewForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author',None)
        self.rew_user = kwargs.pop('rew_user',None)
        
        super(ReviewForm, self).__init__(*args, **kwargs)
   
    class Meta:
        model = Review
        fields = [
                "rating", 
                "text",
                ]
        widgets = {
            "text":forms.Textarea(attrs = {'class' : 'uk-input', 'placeholder' : "Дополнительная информация"} ),
            "rating":forms.widgets.NumberInput(attrs = {'class' : 'uk-input', 'placeholder' : "Введите оценку"} ), 
        }
    def save(self, *args, **kwargs):
        will_commited = kwargs.pop('commit', True)

        obj = super().save(commit=False,*args, **kwargs)
        obj.author = self.author
        obj.user = self.rew_user
        if will_commited:
            obj.save()
        return obj