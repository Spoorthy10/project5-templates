from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "sample2.html")

def hello(request):
    return render(request, "temp/hello.html")

