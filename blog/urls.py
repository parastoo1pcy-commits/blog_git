from django.urls import path, include
from .views import *

app_name='blog'

urlpatterns = [
    path('', BlogListCreateApi.as_view(), name='blog-list-create'),
    path('<int:pk>/', BlogDetailUpdateDeleteApi.as_view(), name='blog-detail-update-delete'),


    # path('list/', BlogListApi.as_view(), name='blog-list'),
    # path('create/', BlogCreateApi.as_view(), name='blog-create'),
    # path('list/<int:pk>/', BlogDetailApi.as_view(), name='blog-detail'),
    # path('update/<int:pk>/', BlogUpdateApi.as_view(), name='blog-update'),
    # path('delete/<int:pk>/', BlogDeleteApi.as_view(), name='blog-delete'),
]