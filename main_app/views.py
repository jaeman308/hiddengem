from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import HiddenGem
from .forms import HiddenGemForm



class HiddenGemCreate(CreateView):
    model = HiddenGem
    from_class = HiddenGemForm

    
def home(request):
    return render(request, 'main_app/home.html')

