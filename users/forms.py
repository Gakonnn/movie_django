from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model =  User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

