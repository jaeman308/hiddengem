from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from main_app.models import HiddenGem, Activity
from .forms import HiddenGemForm, CustomUser, HiddenGemCommentForm




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

def hiddengem_index(request):
    hiddengems = HiddenGem.objects.all()
    return render(request, 'hidden_gem/index.html', {'hiddengems': hiddengems})

def hiddengem_detial(request, hiddengem_id):
    hiddengem = HiddenGem.objects.get(id=hiddengem_id)
    return render(request, 'hidden_gem/detial.html', {'hiddengem': hiddengem})

@login_required
def add_comment(request, hiddengem_id):
    form = HiddenGemCommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.hiddengem_id = hiddengem_id
        new_comment.save()
    return redirect('hiddengem-detial', hiddengem_id=hiddengem_id)



    

