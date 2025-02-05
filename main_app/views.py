from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import HiddenGem


class HiddenGemCreate(CreateView):
    model = HiddenGem
    fields = '__all__'
    
def home(request):
    return render(request, 'main_app/home.html')

