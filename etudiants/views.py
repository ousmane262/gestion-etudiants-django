from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import EtudiantForm

def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')  # on redirigera ici plus tard
    else:
        form = EtudiantForm()
    return render(request, 'etudiants/ajouter.html', {'form': form})

from .models import Etudiant

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiants/liste.html', {'etudiants': etudiants})


from django.shortcuts import get_object_or_404

def modifier_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'etudiants/modifier.html', {'form': form, 'etudiant': etudiant})


def supprimer_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('liste_etudiants')
    return render(request, 'etudiants/supprimer.html', {'etudiant': etudiant})


