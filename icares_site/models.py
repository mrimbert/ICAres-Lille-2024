from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class Epreuve(models.Model):
    nom = models.CharField(max_length=200)
    soustheme = models.CharField(max_length=400)
    description = models.TextField(max_length=3000)
    modalites = models.TextField(max_length=500)
    logo = models.FileField(upload_to="images")
    nombre_de_participant = models.IntegerField(default=0)
    duree = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nom
    

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Crée et sauvegarde un utilisateur avec l'email et le mot de passe haché.
        """
        if not email:
            raise ValueError('Les utilisateurs doivent avoir un email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Utilisation de set_password pour hacher le mot de passe
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Ce champ est géré par AbstractBaseUser
    tel = models.CharField(max_length=20, blank=True)
    ecole = models.CharField(max_length=200)
    isParticipant = models.BooleanField(default=False)
    formule = models.IntegerField()
    epreuve = models.ManyToManyField('Epreuve')

    USERNAME_FIELD = 'email'  # L'email est utilisé comme identifiant unique pour l'authentification
    REQUIRED_FIELDS = ['nom', 'prenom', 'ecole']  # Champs obligatoires en plus du mot de passe

    objects = UserManager()

    def __str__(self):
        return self.email