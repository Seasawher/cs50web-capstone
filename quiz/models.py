from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum

# Create your models here.


class User(AbstractUser):
    pass


class TimeStampedModel(models.Model):
    """abstract base class with timestamp"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class States(Enum):
    TODO = "todo"
    ATTEMPTED = "attempted"
    SOLVED = "solved"


class Quiz(TimeStampedModel):
    """quiz can be solved"""

    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posted_quizzes"
    )
    correct_answer = models.CharField(max_length=50)

    def state(self, user: User) -> States:
        # the all submission the user has posted to the quiz
        submissions = Submission.objects.filter(user=user, quiz=self)

        if submissions.count() > 0:
            quiz_state = States.ATTEMPTED.value
        else:
            quiz_state = States.TODO.value

        for submission in submissions:
            if submission.is_accepted:
                quiz_state = States.SOLVED.value
                break
        return quiz_state

    def is_starred(self, user: User) -> bool:
        """return if the user starred the quiz"""
        return Star.objects.filter(user=user, quiz=self).exists()

    @property
    def star(self) -> int:
        """return the number of stars the quiz has gained"""
        stars = Star.objects.filter(quiz=self)
        return stars.count()


class Star(TimeStampedModel):
    """adding star means the user likes the quiz"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="added_stars")
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="gained_stars"
    )


class Submission(TimeStampedModel):
    """submitted answers to quizzes by users"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="made_submissions"
    )
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="received_submissions"
    )
    submitted_answer = models.CharField(max_length=30, null=True)

    @property
    def is_accepted(self) -> bool:
        """returns if the submission is accepted"""
        quiz = self.quiz
        if self.submitted_answer == quiz.correct_answer:
            return True
        else:
            return False
