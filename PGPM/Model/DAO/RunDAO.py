#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''


from Model.DAO.AgenteDAO import deleteAgenteDir
from Model.Run import Run
import sqlite3 as sql


def listaRun():
	print('mostra tutte le run')
	listaRun = []
	con = sql.connect('database.db')
	cur = con.cursor()
	query = f"SELECT * FROM RUN"
	cur.execute(query)
	print(query)
	result = cur.fetchall()
	if not result:
		print('Nessuna run trovata')
		cur.close()
		return listaRun
	else:
		print('mostro lista run')
		for row in result:
			r = Run(row[0],row[1],row[2],row[3])
			listaRun.append(r)

	cur.close()
	return listaRun

#insert Run
def insertRun(idUtente,idDirectory):
	print('inserisco Run')
	con = sql.connect('database.db')
	cur = con.cursor()
	#creazione query
	query = f"INSERT INTO RUN (UTENTE_ID, TIMESTAMP, DIRECTORY_ID) VALUES ('{idUtente}', CURRENT_TIMESTAMP, '{idDirectory}');"
	cur.execute(query)
	con.commit()
	#print('prima di lastrow')
	lastId = cur.lastrowid
	#print(lastId, '----')
	cur.close()
	print('riuscito inserimento')
	return lastId

def listaRunDirectory(idDirectory):
	print('mostra run della directory')
	listaRun = []
	con = sql.connect('database.db')
	cur = con.cursor()
	print('provo query')
	query = f"SELECT * FROM RUN WHERE DIRECTORY_ID='{idDirectory}';"
	cur.execute(query)
	print(query)
	result = cur.fetchall()
	if not result:
		print('Nessuna run trovata')
		cur.close()
		return listaRun
	else:
		print('mostro lista run')
		for row in result:

			r = Run(row[0],row[1],row[2],row[3])
			listaRun.append(r)

	cur.close()
	return listaRun


def listaRunUtente(idUtente):
	print('mostra tutte le run')
	listaRun = []
	con = sql.connect('database.db')
	cur = con.cursor()
	query = f"SELECT * FROM RUN WHERE UTENTE_ID='{idUtente}';"
	cur.execute(query)
	print(query)
	result = cur.fetchall()
	if not result:
		print('Nessuna run trovata')
		cur.close()
		return listaRun
	else:
		print('mostro lista run')
		for row in result:

			r = Run(row[0],row[1],row[2],row[3])
			listaRun.append(r)

	cur.close()
	return listaRun

def deleteRun(idRun):
	#creazione query
	#Ho bisogno del directory ID
	#Cancello tutti gli agenti che hanno quel directory ID
	#cancello directory che ha quella run_id
	#cancello run che ha idrun
	print('Cancella RUN', idRun)
	print(type(idRun))
	#id_Dir=getDirectoryFromRun(idRun)

	#deleteAgenteDir(id_Dir)
	#deleteDirectoryRun(idRun)

	con = sql.connect('database.db')
	cur = con.cursor()
	
	query = f"DELETE FROM RUN WHERE RUN.ID ='{idRun}';"



	cur.execute(query)
	con.commit()
	print('fetch per vedere se riesce o meno?')
	cur.close()
