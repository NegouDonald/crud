from django.urls import path
from . import views

urlpatterns = [
    path('creer/', views.login, name='login'),
    path('', views.accueil, name='accueil'),
    
    path('login', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('modifier/<int:utilisateur_id>/', views.modifier_utilisateur, name='modifier_utilisateur'),
    path('supprimer/<int:utilisateur_id>/', views.supprimer_utilisateur, name='supprimer_utilisateur'),
]
