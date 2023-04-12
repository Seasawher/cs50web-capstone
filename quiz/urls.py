from django.urls import path

from .views import views, authenticate

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("quiz/<int:quiz_id>", views.Detail.as_view(), name="detail"),
    path("quiz/<int:quiz_id>/addstar", views.AddStar.as_view(), name="addstar"),
    path("quiz/<int:quiz_id>/removestar", views.RemoveStar.as_view(), name="removestar"),
    path("quiz/<int:quiz_id>/submit", views.SubmitAnswer.as_view(), name="submit"),
    path("quiz/add", views.Add.as_view(), name="add"),
    path("login", authenticate.Login.as_view(), name="login"),
    path("logout", authenticate.Logout.as_view(), name="logout"),
    path("register", authenticate.Register.as_view(), name="register"),
]
