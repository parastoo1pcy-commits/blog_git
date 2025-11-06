from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView , DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from blog.models import Blog
from blog.serializers import BlogSerializer

# Create your views here.

class BlogListCreateApi(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]


class BlogDetailUpdateDeleteApi(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]


# class BlogListApi(ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogDetailApi(RetrieveAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogCreateApi(CreateAPIView):
#     serializer_class = BlogSerializer

# class BlogUpdateApi(UpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogDeleteApi(DestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
