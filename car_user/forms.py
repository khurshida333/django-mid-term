from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

# Create your models here.

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserCreationForm,self).__init__(*args, **kwargs)
        for feildname in ['username','password1','password2']:
            self.fields[feildname].help_text=None

class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
