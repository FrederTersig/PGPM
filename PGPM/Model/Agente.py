#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

class Agente:
	#Lista di attributi dell'entità AGENTE
	id, directory_id = 0, 0
	nome, colore = '', ''
	stato , filtro = True, True

	def __init__(self, id,nome, directory_id, colore, stato, filtro):
		print('Modello Agente')
		self.id = id
		self.directory_id = directory_id
		self.nome = nome
		self.colore = colore
		self.stato = stato
		self.filtro = filtro

	#Setter
	def setId(self, id):
		self.id = id
	def setDirectory_id(self, directory_id):
		self.directory_id = directory_id
	def setNome(self, nome):
		self.nome = nome
	def setColore(self,colore):
		self.colore = colore
	def setStato(self,stato):
		self.stato = stato
	def setFiltro(self,filtro):
		self.filtro = filtro

	#Getter
	def getId(self):
		return self.id
	def getDirectory_id(self):
		return self.directory_id
	def getNome(self):
		return self.nome
	def getColore(self):
		return self.colore
	def getStato(self):
		return self.stato
	def getFiltro(self):
		return self.filtro

