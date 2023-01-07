from django.urls import path

from .views import views, authenticate

urlpatterns = [
    path("", views.index, name="index"),
    path("login", authenticate.login_view, name="login"),
    path("logout", authenticate.logout_view, name="logout"),
    path("register", authenticate.register, name="register"),
]
