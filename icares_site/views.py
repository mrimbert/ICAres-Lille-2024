from django.shortcuts import render, get_object_or_404,redirect

from .models import Epreuve

from . import forms

from .forms import CustomLoginForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required



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
            return redirect('custom_login')
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'icares/inscription.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('information')  # Redirige vers la page spéciale après connexion
    else:
        form = CustomLoginForm()

    return render(request, 'icares/connexion.html', {'form': form})

@login_required
def information(request):
    return render(request, 'icares/information.html')