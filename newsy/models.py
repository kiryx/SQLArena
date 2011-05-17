from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
	tytul = models.TextField();
	tresc = models.TextField();
	data_dodania = models.DateTimeField();
	id_autora = models.ForeignKey(User)
	def __unicode__(self):
		return self.tytul
