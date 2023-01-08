from django.urls import path

from .views import views, authenticate

urlpatterns = [
    path("", views.index, name="index"),
    path("login", authenticate.Login.as_view(), name="login"),
    path("logout", authenticate.Logout.as_view(), name="logout"),
    path("register", authenticate.Register.as_view(), name="register"),
]
