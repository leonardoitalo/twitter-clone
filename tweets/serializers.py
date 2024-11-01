from rest_framework import serializers
from .models import UserProfile, Tweet

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'location', 'profile_image']

class TweetSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'author', 'content', 'created_at']
