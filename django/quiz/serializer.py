from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class QuizSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Quiz
        fields = '__all__'
