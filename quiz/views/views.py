from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View
from ..serializer import UserSerializer, QuizSerializer
from ..models import User, Quiz, Submission
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

from ..forms import SubmissionForm

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

    form = SubmissionForm()
    template = "detail.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        quiz_id = kwargs['quiz_id']
        quiz = Quiz.objects.get(pk=quiz_id)
        return render(request, "detail.html", {
            "quiz": quiz,
            "form": self.form
        })


class Add(View):
    """post a new quiz"""

    def get(self, request: HttpRequest, *args, **kwargs):
        pass

    @csrf_exempt
    def post(self, request: HttpRequest, *args, **kwargs):
        user = request.user
        submisson = Submission(
            user = user,
            quiz = kwargs['quiz_id'],
            submitted_answer = request.POST["quiz_id"]
        )
        submisson.save()
