#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

from Model.Directory import Directory
from Model.DAO.AgenteDAO import deleteAgenteDir

import sqlite3 as sql

#Query da fare: Seleziona la directory che ha una tot run_id
# Cancella directory
# Data una run_id , inserisci una nuova directory(1-1)
# data una run_id , ritorna una directory

def deleteDirectoryUtente(idUtente): #Da modificare -> Serve l'id Directory
	con = sql.connect('database.db')
	cur = con.cursor()
	query = f"DELETE FROM DIRECTORY WHERE DIRECTORY.UTENTE_ID ='{idUtente}';"
	cur.execute(query)
	con.commit()
	cur.close()


def deleteDirectory(idDirectory):

	deleteAgenteDir(idDirectory)
	con = sql.connect('database.db')
	cur = con.cursor()
	#creazione query
	query = f"DELETE FROM DIRECTORY WHERE DIRECTORY.ID ='{idDirectory}';"
	cur.execute(query)
	print('fetch per vedere se riesce o meno?')
	con.commit()
	cur.close()

#insert Directory
def insertDirectory(utente_id, path,nome):
	print('inserisco Directory')
	con = sql.connect('database.db')
	cur = con.cursor()
	#creazione query
	query = f"INSERT INTO DIRECTORY(UTENTE_ID, PATH, NOME) VALUES ('{utente_id}', '{path}', '{nome}');"
	cur.execute(query)
	con.commit()
	lastId = cur.lastrowid
	cur.close()
	print('riuscito inserimento')
	return lastId

#def getDirectoryFromRun(run_id): #CERCA E CAMBIA
#	print('prendo directory')
#	con = sql.connect('database.db')
#	cur = con.cursor()
#	query = f"SELECT ID FROM DIRECTORY WHERE DIRECTORY.RUN_ID ='{run_id}';"
#	cur.execute(query)
#	res = cur.fetchone()
#	cur.close()
#	print('directory--- ', list(res))
#	return list(res)[0]

def getDirectory(utente_id): #CERCA E CAMBIA
	print('prendo directory')
	listaDirectory=[]
	con = sql.connect('database.db')
	cur = con.cursor()
	try:
		query = f"SELECT * FROM DIRECTORY WHERE DIRECTORY.UTENTE_ID ='{utente_id}';"
		cur.execute(query)
		result = cur.fetchall()
		if not result: #Risultato vuoto
			print('Nessuna Directory presente')
			cur.close()
			return listaDirectory
		else:
			#print('Mostro lista utenti')
			#print(result)
			#print('-------')
			for row in result:

				u = Directory(row[0],row[1],row[2],row[3])
				listaDirectory.append(u)
		
	except TypeError:
		print('Exception TypeError')
	cur.close()
	return listaDirectory



		#row = list(res)

		#u = Directory(row[0],row[1],row[2],row[3])
		#cur.close()
	#except TypeError:
	#	u = None
	#return u

	

def listaDirectory():
	print('lista di tutte le directory')
	listaDirectory=[]
	con = sql.connect('database.db')
	cur = con.cursor()
	query = f"SELECT * FROM DIRECTORY;"
	cur.execute(query)
	result = cur.fetchall()
	if not result: #Risultato vuoto
		print('Nessun utente presente')
		cur.close()
		return listaDirectory
	else:
		#print('Mostro lista utenti')
		#print(result)
		#print('-------')
		for row in result:
			u = Directory(row[0],row[1],row[2],row[3])
			listaDirectory.append(u)
	cur.close()
	return listaDirectory







