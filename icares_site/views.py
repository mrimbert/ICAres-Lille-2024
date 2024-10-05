from django.shortcuts import render, get_object_or_404,redirect

from .models import Epreuve, create_user_groups, Lien

from . import forms

from .forms import CustomLoginForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    create_user_groups(None)
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
            return redirect('connexion')
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
    lien = list(Lien.objects.filter(id=1).values()[0].values())

    if request.method == 'POST':
        form = forms.UserUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = forms.UserUpdateForm(instance=request.user)

    
    return render(request, 'icares/information.html', context={"form":form, "lien":lien})