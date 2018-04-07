from django.forms import ModelForm
from .models import Produit

class ProduitForm(ModelForm):
	class Meta:
		model = Produit
		fields = ['nom','photo','p_ttc']
