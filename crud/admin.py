from django.contrib import admin
from .models import Utilisateur

# Enregistrement du modèle Utilisateur dans l'admin
@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')  # Colonnes affichées dans la liste
    search_fields = ('nom', 'email')  # Ajoute une barre de recherche
    list_filter = ('prenom',)  # Filtres sur le côté
