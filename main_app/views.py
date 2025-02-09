from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .models import HiddenGem
from .forms import HiddenGemForm



class HiddenGemCreate(CreateView):
    model = HiddenGem
    form_class = HiddenGemForm


    
def home(request):
    return render(request, 'main_app/home.html')


class Login(LoginView):
    template_name = 'registration/login.html'

