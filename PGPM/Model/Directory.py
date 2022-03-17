#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

class Directory:

	id, utente_id = 0,0
	nome, path = '',''

	def __init__(self,id,nome,path,utente_id):
		print('Modello Directory')
		self.id=id
		self.utente_id = utente_id
		self.nome = nome
		self.path = path

	#Setter
	def setId(self,id):
		self.id=id
	def setUtente_id(self,utente_id):
		self.utente_id=utente_id
	def setNome(self,nome):
		self.nome=nome
	def setPath(self,path):
		self.path=path

	#Getter

	def getId(self):
		return self.id
	def getUtente_id(self):
		return self.utente_id
	def getNome(self):
		return self.nome
	def getPath(self):
		return self.path