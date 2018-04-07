from django.shortcuts import render
from .models import Produit
from .forms import ProduitForm
# Create your views here.

def accueil(request):
	listProd = Produit.objects.all()
	return render(request, 'index.html', locals())


def saisir(request):
	sauvegarde = False
	form = ProduitForm(request.POST or None, request.FILES)
	if form.is_valid():
		nouvProd = Produit()
		nouvProd.nom = form.cleaned_data["nom"]
		nouvProd.photo = form.cleaned_data["photo"]
		nouvProd.p_ttc = form.cleaned_data["p_ttc"]
		nouvProd.save()
		sauvegarde = True
	return render(request, 'saisie.html', locals())
		
