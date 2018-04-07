from django.db import models

# Create your models here.

class Produit(models.Model):
	nom = models.CharField(max_length=100)
	photo = models.ImageField(upload_to="photos/")
	p_ttc = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = "Prix unitaire TTC")
	def __str__(self):
		return self.nom
	
