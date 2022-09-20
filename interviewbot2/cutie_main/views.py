from django.shortcuts import render
from . import views


# Create your views here.
def index(request):
    return render(request, "cutie_main/index.html", {})


def home(request):
    return render(request, "cutie_main/home.html", {})
