from django.shortcuts import render

from .models import Epreuve
# Create your views here.

def index(request):
    return render(request, "icares/index.html")

def epreuve(request):

    epreuve_query = Epreuve.objects.all()

    context = {"epreuve":epreuve_query}
    return render(request, "icares/epreuve.html", context)
