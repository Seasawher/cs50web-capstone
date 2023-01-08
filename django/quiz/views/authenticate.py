from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views import View

from ..forms import LoginForm, RegisterForm
from ..models import User


class Login(View):
    form = LoginForm()
    template = "login.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, self.template, {"form": self.form})

    def post(
        self, request: HttpRequest, *args, **kwargs
    ) -> HttpResponse | HttpResponseRedirect:
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                self.template,
                {"message": "Invalid username and/or password."},
            )


class Logout(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponseRedirect:
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class Register(View):
    form = RegisterForm()
    template = "register.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, self.template, {"form": self.form})

    def post(
        self, request: HttpRequest, *args, **kwargs
    ) -> HttpResponse | HttpResponseRedirect:
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, self.template, {"message": "Passwords must match."})

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, self.template, {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
