from django import forms
from .models import HiddenGem, Activty
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class HiddenGemForm(forms.ModelForm):
    class Meta:
        model = HiddenGem
        fields = ['title', 'category', 'location', 'description']

class CustomUser(UserCreationForm):
    email = forms. EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    las_name= forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields= ['username', 'first_name', 'las_name', 'email', 'password1', 'password2']