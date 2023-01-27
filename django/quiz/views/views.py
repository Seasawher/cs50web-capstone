from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View
from ..serializer import *
from ..models import *
from rest_framework import viewsets

from ..forms import *

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class Index(View):
    """diplay quizzes"""

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "index.html")


class Detail(View):
    """show the detail info of the quiz"""
    form = Submission()
    template = "detail.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "detail.html", {"form": self.form})


class Add(View):
    """post a new quiz"""

    def get(self, request: HttpRequest, *args, **kwargs):
        pass

    def post(self, request: HttpRequest, *args, **kwargs):
        pass
