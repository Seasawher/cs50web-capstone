from rest_framework import serializers

from .models import User, Quiz


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class QuizSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    gained_stars = serializers.Field()

    def gained_stars(self, obj):
        return obj.gained_stars

    class Meta:
        model = Quiz
        fields = ("id", "user", "created_at", "title", "gained_stars", "content")
