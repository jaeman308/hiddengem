from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('userhome/', views.userhome, name='userhome'),
    path('login/', views.Login.as_view(), name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('hiddengem/create/', views.HiddenGemCreate.as_view(), name='hiddengem-create'),
    path('hiddengems/', views.hiddengem_index, name='hiddengem-index'),
    path('hiddengems/<int:hiddengem_id>/', views.hiddengem_detail, name='hiddengem-detail'),
]