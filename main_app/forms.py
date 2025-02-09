from django import forms
from .models import HiddenGem, Activty


class HiddenGemForm(forms.ModelForm):
    class Meta:
        model = HiddenGem
        fields = ['title', 'category', 'location', 'description']
