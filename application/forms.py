from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField( required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')