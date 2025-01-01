from django.db import models

# Create your models here.
from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, default="Inconnu")
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
