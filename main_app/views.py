from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from main_app.models import HiddenGem
from .forms import HiddenGemForm, CustomUser




class HiddenGemCreate(LoginRequiredMixin, CreateView):
    model = HiddenGem
    form_class = HiddenGemForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

class Login(LoginView):
    template_name = 'registration/login.html'



def home(request):
    return render(request, 'main_app/home.html')


@login_required
def userhome(request):
    return render(request, 'main_app/user_home.html')


def signup(request): 
    error_message= ''
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            user = form.save()
            log(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try agian'
    else: 
        form = CustomUser
    context = {'form': form, 'error_message': error_message}
    return render(request, 'main_app/signup.html', context)

        



    

