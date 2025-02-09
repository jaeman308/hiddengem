from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('hiddengem/create/', views.HiddenGemCreate.as_view(), name='hiddengem-create'),
]