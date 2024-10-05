from django import forms
from .models import User, Epreuve
from django.contrib.auth import authenticate


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmez le mot de passe')

    # Options pour les choix
    ECOLE_CHOICES = [
        ('Lyon', 'Lyon'),
        ('Lille', 'Lille'),
        ('Marseille', 'Marseille'),
        ('Paris', 'Paris'),
        ('Nantes', 'Nantes'),
    ]

    FORMULE_CHOICES = [
        (1, 'Entrée'),
        (2, 'Entrée + Repas'),
        (3, 'Entrée + Repas + Logement'),
    ]

    PARTICIPANT_CHOICES = [
        (0, 'Participant'),
        (1, 'Spectateur'),
        (2, 'Jury'),
    ]

    # Champs du formulaire
    ecole = forms.ChoiceField(choices=ECOLE_CHOICES, label='École')
    formule = forms.ChoiceField(choices=FORMULE_CHOICES, label='Formule')
    isParticipant = forms.ChoiceField(choices=PARTICIPANT_CHOICES, label='Statut')

    class Meta:
        model = User
        fields = ['nom', 'prenom', 'email', 'tel', 'ecole', 'isParticipant', 'formule', 'epreuve']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hachage du mot de passe
        if commit:
            user.save()
        return user
    

class CustomLoginForm(forms.Form):
    email = forms.EmailField(label='Email')  # On utilise 'email' au lieu de 'username'
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if not user:
            raise forms.ValidationError("Email ou mot de passe incorrect.")
        return self.cleaned_data
    


class UserUpdateForm(forms.ModelForm):
    ECOLE_CHOICES = [
        ('Lyon', 'Lyon'),
        ('Lille', 'Lille'),
        ('Marseille', 'Marseille'),
        ('Paris', 'Paris'),
        ('Nantes', 'Nantes'),
    ]

    FORMULE_CHOICES = [
        (1, 'Entrée'),
        (2, 'Entrée + Repas'),
        (3, 'Entrée + Repas + Logement'),
    ]

    PARTICIPANT_CHOICES = [
        (0, 'Participant'),
        (1, 'Spectateur'),
        (2, 'Jury'),
    ]

    ecole = forms.ChoiceField(choices=ECOLE_CHOICES, label='École')
    formule = forms.ChoiceField(choices=FORMULE_CHOICES, label='Formule')
    isParticipant = forms.ChoiceField(choices=PARTICIPANT_CHOICES, label='Statut')

    class Meta:
        model = User
        fields = ['nom', 'prenom', 'email', 'tel', 'ecole', 'isParticipant', 'formule', 'epreuve']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user