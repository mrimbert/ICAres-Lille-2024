from django.db import models

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