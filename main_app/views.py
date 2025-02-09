from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .models import HiddenGem
from .forms import HiddenGemForm, CustomUser



class HiddenGemCreate(CreateView):
    model = HiddenGem
    form_class = HiddenGemForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Login(LoginView):
    template_name = 'registration/login.html'

   
def home(request):
    return render(request, 'main_app/home.html')

def userhome(request):
    return render(request, 'main_app/user_home.html')


def signup(request): 
    error_message= ''
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            user = form.save()
            log(request, user)
            return redirect(hiddengem-index)
        else:
            error_message = 'Invalid sign up - try agian'
    else: 
        form = CustomUser
    context = {'form': form, 'error_message': error_message}
    return render(request, 'main_app/signup.html', context)

        



    

