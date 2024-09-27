from django.shortcuts import render, get_object_or_404,redirect

from .models import Epreuve

from . import forms

import json

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


def register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            return redirect('login')
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'icares/inscription.html', {'form': form})