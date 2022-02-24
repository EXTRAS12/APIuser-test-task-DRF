from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'other_name', 'email', 'phone', 'birthday',
                  'city', 'additional_info', 'is_admin']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'other_name', 'email', 'phone', 'birthday',
                  'city', 'additional_info', 'is_admin']
