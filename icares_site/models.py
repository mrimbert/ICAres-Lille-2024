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
        if not email:
            raise ValueError('L\'utilisateur doit avoir un email valide')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le super utilisateur doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le super utilisateur doit avoir is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Ce champ est géré par AbstractBaseUser
    tel = models.CharField(max_length=20, blank=True)
    ecole = models.CharField(max_length=200)
    isParticipant = models.BooleanField(default=False)
    formule = models.IntegerField(default=0)
    epreuve = models.ManyToManyField('Epreuve')


    is_active = models.BooleanField(default=True)  # Utilisateur actif ou non
    is_staff = models.BooleanField(default=False)  # Indique si l'utilisateur est membre du staff (accès admin)
    is_superuser = models.BooleanField(default=False)  # Indique si l'utilisateur est super utilisateur (droits complets)

    USERNAME_FIELD = 'email'  # L'email est utilisé comme identifiant unique pour l'authentification
    REQUIRED_FIELDS = ['nom', 'prenom', 'ecole']  # Champs obligatoires en plus du mot de passe

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True