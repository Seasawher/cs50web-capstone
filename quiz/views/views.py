from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from ..models import User, Quiz, Submission, Star
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.paginator import Paginator, Page
from typing import List
from django.db.models import Model


from ..forms import SubmissionForm, AddQuizForm

# Create your views here.


class Index(View):
    """diplay quizzes"""

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        quizzes = Quiz.objects.all()

        if request.user.is_authenticated:
            # add property
            for quiz in quizzes:
                quiz.quiz_state = quiz.state(request.user)
                quiz.request_user = request.user
        else:
            for quiz in quizzes:
                quiz.quiz_state = "todo"
                quiz.starred = False

        page_obj = paginate(request, quizzes)

        return render(request, "index.html", {"page_obj": page_obj})


def paginate(request: HttpRequest, model_objects: List[Model]) -> Page:
    """
    create Page object to display 5 quizzes per page
    """
    paginator = Paginator(model_objects, 5)
    page_number = request.GET.get("page") or 1
    page_obj = paginator.get_page(page_number)
    return page_obj


class Detail(View):
    """show the detail info of the quiz"""

    form = SubmissionForm()
    template = "detail.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        quiz_id = kwargs["quiz_id"]
        quiz = Quiz.objects.get(pk=quiz_id)

        if request.user.is_authenticated:
            state = quiz.state(request.user)
            quiz.request_user = request.user
        else:
            state = "todo"
            quiz.starred = False

        return render(
            request,
            "detail.html",
            {"quiz": quiz, "state": state, "form": self.form},
        )


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
            correct_answer=request.POST["correct_answer"],
        )
        quiz.save()
        messages.success(request, "Submitted successfully!")
        return render(request, "add.html", {"form": self.form})


@method_decorator(login_required, name="dispatch")
class SubmitAnswer(View):
    form = SubmissionForm()

    def post(self, request: HttpRequest, *args, **kwargs):
        # get quiz id from url
        quiz_id = kwargs["quiz_id"]
        quiz = Quiz.objects.get(pk=quiz_id)

        # save user's submission
        submission = Submission(
            user=request.user,
            quiz=quiz,
            submitted_answer=request.POST["submitted_answer"],
        )
        submission.save()

        # check if the answer is correct
        if quiz.correct_answer == submission.submitted_answer:
            messages.success(request, "Your answer is accepted!")
            return render(
                request,
                "detail.html",
                {"quiz": quiz, "form": self.form, "state": "solved"},
            )
        else:
            messages.error(request, "Your answer is not correct!")
            state = quiz.state(request.user)
            return render(
                request,
                "detail.html",
                {"quiz": quiz, "form": self.form, "state": state},
            )


@method_decorator(login_required, name="dispatch")
@method_decorator(csrf_exempt, name="dispatch")
class AddStar(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        """post a new star to the quiz"""
        quiz_id = kwargs["quiz_id"]
        quiz = Quiz.objects.get(pk=quiz_id)
        user = request.user

        # search existing star
        if not Star.objects.filter(user=user, quiz=quiz).exists():
            star = Star(user=user, quiz=quiz)
            star.save()
        return JsonResponse({"message": "Star added successfully."}, status=204)


@method_decorator(login_required, name="dispatch")
@method_decorator(csrf_exempt, name="dispatch")
class RemoveStar(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        """delete a star from the quiz"""
        quiz_id = kwargs["quiz_id"]
        quiz = Quiz.objects.get(pk=quiz_id)
        user = request.user
        Star.objects.filter(user=user, quiz=quiz).delete()
        return JsonResponse({"message": "Star removed successfully."}, status=204)


@method_decorator(login_required, name="dispatch")
class Profile(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        """display the user's profile page"""
        host_user_id = kwargs["user_id"]
        host_user = User.objects.get(pk=host_user_id)
        submissions = host_user.made_submissions.order_by("created_at").reverse()
        submissions = submissions[:10]
        return render(
            request,
            "profile.html",
            {"submissions": submissions, "host_user": host_user},
        )
