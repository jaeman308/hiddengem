from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('hiddengem/create/', views.HiddenGemCreate.as_view(), name='hiddengem-create'),
    path('hiddengems/', views.hiddengem_index, name='hiddengem-index'),
    path('hiddengems/<int:hiddengem_id>/', views.hiddengem_detail, name='hiddengem-detail'),
    path('hiddengems/<int:pk>/update/', views.HiddenGemUpdate.as_view(), name='hiddengem-update'),
    path('hiddengems/<int:pk>/delete/', views.HiddenGemDelete.as_view(), name='hiddengem-delete'),
    path('hiddengems/<int:hiddengem_id>/add-comment/', views.HiddengemCommentCreate.as_view(), name='add-comment'),
]