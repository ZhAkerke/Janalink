from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, NewsPost, Comment

# 1. ModelSerializer — for news
class NewsPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = NewsPost
        fields = '__all__'

# 2. ModelSerializer — for comments
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = '__all__'

# 3. Serializer — for registrations
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

# 4. Serializer — for logins
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

from rest_framework import serializers
from .models import Comment

# General Serializer (не ModelSerializer)
class CommentManualSerializer(serializers.Serializer):
    content = serializers.CharField()
    date_posted = serializers.DateTimeField(read_only=True)

# ModelSerializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
