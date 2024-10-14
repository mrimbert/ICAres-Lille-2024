from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Lien(models.Model):
    lille = models.CharField(max_length=300, default="None")
    lyon = models.CharField(max_length=300, default="None")
    paris = models.CharField(max_length=300, default="None")
    marseille = models.CharField(max_length=300, default="None")
    nantes = models.CharField(max_length=300, default="None")

class Epreuve(models.Model):
    nom = models.CharField(max_length=200)
    soustheme = models.CharField(max_length=400)
    description = models.TextField(max_length=3000)
    modalites = models.TextField(max_length=1000)
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

class User(AbstractBaseUser, PermissionsMixin):

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

    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=20, blank=True)
    ecole = models.CharField(max_length=200)
    isParticipant = models.IntegerField(choices=PARTICIPANT_CHOICES,default=0, verbose_name="Etat")
    formule = models.IntegerField(choices=FORMULE_CHOICES, null=True, blank=True)
    epreuve = models.ManyToManyField('Epreuve')
    has_paid = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom']

    objects = UserManager()

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.email})"
    


def create_user_groups(sender, **kwargs):
    # Création des groupes
    organisateur, _ = Group.objects.get_or_create(name='Organisateur')
    tresorier, _ = Group.objects.get_or_create(name='Trésorier')

    # Obtenir le content type du modèle User
    user_content_type = ContentType.objects.get_for_model(User)
    epreuve_content_type = ContentType.objects.get_for_model(Epreuve)
    lien_content_type = ContentType.objects.get_for_model(Lien)

    # Permissions Organisateur (trésorier) -> Voir Nom, Prénom, Formule, Épreuves + Export CSV
    organisateur_permissions = Permission.objects.filter(
        content_type=user_content_type,
        codename__in=['view_user', 'export_csv', 'change_user', 'mark_as_paid', "view_epreuve", "change_epreuve", "add_epreuve"]
    )
    organisateur.permissions.set(organisateur_permissions)

    epreuve_permissions = Permission.objects.filter(
        content_type=epreuve_content_type
    )
    organisateur.permissions.add(*epreuve_permissions)

    lien_permissions = Permission.objects.filter(
        content_type = lien_content_type,
    )
    organisateur.permissions.add(*lien_permissions)

    # Permissions Trésorier des autres écoles -> Voir Nom, Prénom, Formule, Épreuves + Gestion paiement
    tresorier_autres_permissions = Permission.objects.filter(
        content_type=user_content_type,
        codename__in=['view_user', 'mark_as_paid', 'export_csv']
    )
    tresorier.permissions.set(tresorier_autres_permissions)