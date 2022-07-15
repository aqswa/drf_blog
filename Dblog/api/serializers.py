from dataclasses import field
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'comment']


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        login_id = validated_data.get('login_id')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User(
            login_id=login_id,
            email=email
        )
        user.set_password(password)
        user.save()
        return user
