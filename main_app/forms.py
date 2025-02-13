from django import forms
from .models import HiddenGem, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class HiddenGemForm(forms.ModelForm):
    class Meta:
        model = HiddenGem
        fields = ['title', 'category', 'location', 'description']

class CustomUser(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name= forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class HiddenGemCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        field = ["author", "commenttext"]