#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''


class Run: 

	id,utente_id, directory_id = 0,0,0
	timestamp = 'DATA ????'

	def __init__(self,id,utente_id,timestamp,directory_id):
		print('Modello Run')
		self.id = id
		self.utente_id = utente_id
		self.directory_id = directory_id
		self.timestamp = timestamp

	#setter
	def setId(self, id):
		self.id = id
	def setUtente_id(self,utente_id):
		self.utente_id = utente_id
	def setTimestamp(self,timestamp):
		self.timestamp = timestamp
	def setDirectory_Id(self,directory_id):
		self.directory_id=directory_id
	
	#getter
	
	def getId(self):
		return self.id
	def getUtente_id(self):
		return self.utente_id
	def getTimestamp(self):
		return self.timestamp
	def getDirectory_id(self):
		return self.directory_id