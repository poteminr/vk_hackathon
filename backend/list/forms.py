from django import forms
from list.models import *

from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(PostForm, self).__init__(*args, **kwargs)
   
    class Meta:
        model = Post
        fields = [
                "title", 
                "text",
                "cost",
                "image",
                ]
        widgets = {
            "title": forms.TextInput(attrs = {'class' : 'uk-input', 'placeholder' : "Название"} ),
            "text":forms.Textarea(attrs = {'class' : 'uk-input', 'placeholder' : "Дополнительная информация"} ),
            "cost":forms.widgets.NumberInput(attrs = {'class' : 'uk-input', 'placeholder' : "COST"} ), 
        }

    def save(self, *args, **kwargs):
        will_commited = kwargs.pop('commit', True)

        obj = super().save(commit=False,*args, **kwargs)
        obj.employer = self.user
        if will_commited:
            obj.save()
        return obj
