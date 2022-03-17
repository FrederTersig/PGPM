#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

class Utente:

	idUtente = 0
	nome, email = '',''
	password = ''
	ruolo = 0

	def __init__(self,idUtente,nome, email, password, ruolo):
		print('Modello Utente')
		self.idUtente = idUtente
		self.nome = nome
		self.email = email
		self.password = password
		self.ruolo = ruolo

		#Setter
	def setId(self,idUtente):
		self.idUtente=idUtente
	def setRuolo(self,ruolo):
		self.ruolo=ruolo
	def setNome(self,nome):
		self.nome=nome
	def setEmail(self,email):
		self.email=email
	def setPassword(self,password): # SHA456 <-- encrypt 
		self.password=password

	#Getter

	def getId(self):
		return self.idUtente
	def getRuolo(self):
		return self.ruolo
	def getNome(self):
		return self.nome
	def getEmail(self):
		return self.email
	def getPassword(self): # SHA456 <-- decrypt
		return self.password
	