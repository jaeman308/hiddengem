from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('hiddengem/create/', views.HiddenGemCreate.as_view(), name='hiddengem-create'),
]