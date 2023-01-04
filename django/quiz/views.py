from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpRequest

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "quiz/index.html")
