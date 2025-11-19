from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'), 
    path('user/', UserListCreateApi.as_view(), name='userceate'),
    path('user/<int:pk>/', UserDetailUpdateDeleteApi.as_view(), name='userdeleteupdatedetail'),    
]