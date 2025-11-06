from rest_framework import serializers 
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta :
        model=Blog
        # fields = ['title', 'body']
        fields = "__all__"
        # exlude = ['created_at', 'images']