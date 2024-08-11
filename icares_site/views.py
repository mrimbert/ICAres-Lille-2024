from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "icares/index.html")

def epreuve(request):
    return render(request, "icares/epreuve.html")
