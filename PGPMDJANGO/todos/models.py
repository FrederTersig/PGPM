from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Utente(AbstractUser):
	id = models.BigAutoField(primary_key=True)
	nome = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=70)
	ruolo = models.SmallIntegerField()



class Directory(models.Model):
	id = models.BigAutoField(primary_key=True)
	run_id = models.ForeignKey(
		'Run',
		on_delete=models.CASCADE,
		)
	nome = models.CharField(max_length=20)
	path = models.CharField(max_length=70)


class Agente(models.Model):
	id = models.BigAutoField(primary_key=True)
	directory_id = models.ForeignKey(
		'Directory',
		on_delete=models.CASCADE,
		)
	nome = models.CharField(max_length=20)
	colore = models.CharField(max_length=20)
	stato = models.SmallIntegerField()
	filtro = models.SmallIntegerField()



class Run(models.Model):
	id = models.BigAutoField(primary_key=True)
	utente_id = models.ForeignKey(
		'Utente',
		on_delete=models.CASCADE,
		)
	timestamp = models.DateTimeField(auto_now_add=True)
	#relDirectory = models.OneToOneField(Directory, on_delete=models.CASCADE)




