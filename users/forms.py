from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label= ("Password"),
        widget=forms.PasswordInput,
        strip=False,
    )
    password2 = forms.CharField(
        label= ("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
    )
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')