from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View
from ..serializer import *
from ..models import *
from rest_framework import viewsets

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


class AddQuiz(View):
    """post a new quiz"""

    def get(self, request: HttpRequest, *args, **kwargs):
        pass

    def post(self, request: HttpRequest, *args, **kwargs):
        pass
