from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from ..models import User

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")
