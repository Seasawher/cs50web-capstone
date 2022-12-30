from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class TimeStampedModel(models.Model):
    """abstract base class with timestamp"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Quiz(TimeStampedModel):
    """quiz can be solved"""

    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posted_quizzes"
    )
    correct_answer = models.TextField()


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
    is_correct = models.BooleanField()
