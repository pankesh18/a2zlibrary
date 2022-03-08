from dataclasses import field
import email
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields =    [ 'username', 'email', 'password1', 'password2'  ]
        





class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields =    [ 'username', 'email']



# class UserPasswordUpdateForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields =   [ 'password1', 'password2' ]       





class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields =    [ 'image' ]
