from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from main_app.models import HiddenGem, Activity, User, Comment
from django.contrib.auth import login
from .forms import HiddenGemForm, CustomUser, HiddenGemCommentForm
from .filters import HiddenGemFilter, UserHiddenGemFilter




class HiddenGemCreate(LoginRequiredMixin, CreateView):
    model = HiddenGem
    form_class = HiddenGemForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class HiddenGemUpdate(LoginRequiredMixin, UpdateView):
    model= HiddenGem
    form_class = HiddenGemForm
    template_name= 'main_app/update.html'
    
    def get_successs_url(self):
         return reverse('hiddengem-detail', kwargs={'pk': self.object.pk})



class HiddenGemDelete(LoginRequiredMixin, DeleteView):
    model = HiddenGem
    success_url='/hiddengems/'


class Login(LoginView):
    template_name = 'registration/login.html'


class HiddengemCommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = HiddenGemCommentForm
    template_name= "hidden_gem/hiddengemComment_form.html"
    success_url = '/hiddengems/<int:hiddengem_id>/'



def home(request):
    return render(request, 'main_app/home.html')


@login_required
def userhome(request):
    user = request.user
    hiddengems = HiddenGem.objects.filter(user=user)
    hiddengem_filter = UserHiddenGemFilter(request.GET, queryset=hiddengems)
    return render(request, 'main_app/user_home.html', {'user': user, "hiddengems": hiddengems, 'filter': hiddengem_filter })


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
        form = CustomUser()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'main_app/signup.html', context)

@login_required
def hiddengem_index(request):
    hiddengems = HiddenGem.objects.all()
    hiddengem_filter = HiddenGemFilter(request.GET, queryset=hiddengems)
    return render(request, 'hidden_gem/index.html', {'hiddengems': hiddengems, 'filter': hiddengem_filter})


@login_required
def hiddengem_detail(request, hiddengem_id):
    hiddengem = HiddenGem.objects.get(id=hiddengem_id)
    comments = Comment.objects.filter(hiddengem=hiddengem)
    return render(request, 'hidden_gem/detail.html', {'hiddengem': hiddengem, "comments": comments})

