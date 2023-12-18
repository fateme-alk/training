# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, "training/base.html")


def about(request):
    return render(request, "training/about.html")


def contact(request):
    return render(request, "training/contact.html")


def classes(request):
    return render(request, "training/classes.html")
