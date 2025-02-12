from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('userhome/', views.userhome, name='userhome'),
    path('login/', views.Login.as_view(), name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('hiddengem/create/', views.HiddenGemCreate.as_view(), name='hiddengem-create'),
    path('hiddengem/<int:pk>/update', views.HiddenGemUpdate.as_view(), name'hiddengem-update'),
    path('hiddengem/<int:pk>/delete', views.HiddenGemDelete.as_view(), name='hiddengem-delete'),
]