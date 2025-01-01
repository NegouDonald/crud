from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Utilisateur

# Créer un utilisateur


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Utilisateur

def login(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('mot_de_passe')

        # Vérifier si l'email existe déjà
        if Utilisateur.objects.filter(email=email).exists():
            messages.error(request, "cette ulisateur existe déjà.")
            return redirect('login')  # Rediriger vers la page de création avec un message d'erreur

        # Sinon, créer l'utilisateur
        utilisateur = Utilisateur(nom=nom, prenom=prenom, email=email, mot_de_passe=mot_de_passe)
        utilisateur.save()
        messages.success(request, "Utilisateur créé avec succès.")
        return redirect('liste_utilisateurs')  # Rediriger vers la page d'accueil ou une autre page

    return render(request, 'login.html')



# Lire tous les utilisateurs
def liste_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    return render(request, 'liste_utilisateurs.html', {'utilisateurs': utilisateurs})

# Modifier un utilisateur
def modifier_utilisateur(request, utilisateur_id):
    utilisateur = get_object_or_404(Utilisateur, id=utilisateur_id)
    if request.method == "POST":
        utilisateur.nom = request.POST['nom']
        utilisateur.nom = request.POST['prenom']
        utilisateur.email = request.POST['email']
        utilisateur.mot_de_passe = request.POST['mot_de_passe']
        utilisateur.save()
        return redirect('liste_utilisateurs')
    return render(request, 'modifier_utilisateur.html', {'utilisateur': utilisateur})

# Supprimer un utilisateur
def supprimer_utilisateur(request, utilisateur_id):
    utilisateur = get_object_or_404(Utilisateur, id=utilisateur_id)
    utilisateur.delete()
    return redirect('liste_utilisateurs')

from django.shortcuts import render

def accueil(request):
    return render(request, 'accueil.html')
