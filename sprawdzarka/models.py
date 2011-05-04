from django.db import models 
from django.contrib.auth.models import User

class Baza(models.Model):
	nazwa = models.CharField(max_length=20)
	skrypt = models.TextField()
	
class Problem(models.Model):
	tresc = models.TextField()
	rozwiazanie = models.TextField()
	id_bazy = models.ForeignKey(Baza)
	id_autora = models.ForeignKey(User)
	
class ProblemUser(models.Model):
	id_uzytkownika = models.ForeignKey(User)
	id_problemu = models.ForeignKey(Problem)
	status = models.IntegerField()
	odpowiedz = models.TextField()

# Create your models here.
