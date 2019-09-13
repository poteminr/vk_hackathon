from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Review


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','is_local_admin', 'email']
    list_filter = ('is_local_admin',)


    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('name','additionalinfo','is_local_admin', 'photo')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1','password2')}),
        ('Personal info', {'fields': ('name','additionalinfo','is_local_admin', 'photo')}),
    )
    
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Review)
