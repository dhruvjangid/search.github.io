from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("hello world")


def dhruv(request):
    return HttpResponse("hello dhruv jangid")

def greet(request, name):
    return render(request,"helloo/greet.html",
    {
        "name":name.capitalize()
    })