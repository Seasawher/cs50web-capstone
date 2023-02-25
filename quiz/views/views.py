from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.views import View
from ..serializer import UserSerializer, QuizSerializer
from ..models import User, Quiz
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..forms import SubmissionForm, AddQuizForm

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
        quiz_id = kwargs["quiz_id"]
        quiz = Quiz.objects.get(pk=quiz_id)
        return render(request, "detail.html", {"quiz": quiz, "form": self.form})


@method_decorator(login_required, name="dispatch")
class Add(View):
    """post a new quiz"""

    form = AddQuizForm()

    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, "add.html", {"form": self.form})

    def post(self, request: HttpRequest, *args, **kwargs):
        user = request.user
        quiz = Quiz(
            user=user,
            title=request.POST["title"],
            content=request.POST["content"],
            correct_answer=request.POST["correct_answer"]
        )
        quiz.save()
        return redirect("add")
