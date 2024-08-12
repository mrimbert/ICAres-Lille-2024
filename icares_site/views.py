from django.shortcuts import render, get_object_or_404

from .models import Epreuve
# Create your views here.

def index(request):
    return render(request, "icares/index.html")

def epreuve(request):

    epreuve_query = Epreuve.objects.all()

    context = {"epreuve":epreuve_query}
    return render(request, "icares/epreuve.html", context)

def detail(request, id):
    epreuve_get = get_object_or_404(Epreuve, id=id)  

    context = {"epreuve":epreuve_get}

    return render(request, "icares/detail.html", context)
