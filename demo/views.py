from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def greet(request):
    return render(request, 'demo/Hello.html', {"name": "Joy"})


def greet_me(request, name):
    return HttpResponse(f"Let's xplore django together {name}")
