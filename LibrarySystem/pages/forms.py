from django.forms import fields
from pages import models
from django import forms
from .models import addbook, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import PasswordInput


class LoginForm(forms.ModelForm):
    username = forms.CharField(label= 'Username', required=True)
    password = forms.CharField(label= 'Password', required=True, widget=forms.PasswordInput())
    class Meta:
        model = Profile
        fields = ('username', 'password')


class CreationUserForm(UserCreationForm):
    
    username = forms.CharField(label='Username', required=True)
    email = forms.EmailField(label='Email', required=True)
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirmation Password', required=True, widget=forms.PasswordInput())
    '''group = forms.CharField(label='User Type',null=False, choices=x)'''
    class Meta:
        model = User
        
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        
        fields = ('user', 'name', 'email', 'gender', 'books')