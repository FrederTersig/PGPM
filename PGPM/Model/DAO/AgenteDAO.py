#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
from Model.Agente import Agente
import sqlite3 as sql



#cancella
#insert agente (serve directory_id)
#dato directory_id, ritorna tutti agenti

def deleteAgenteDir(idDir):
	try:
		con = sql.connect('database.db')
		cur = con.cursor()
		query = f"DELETE FROM AGENTE WHERE AGENTE.DIRECTORY_ID='{idDir}';"
		cur.execute(query)
		con.commit()
	except Exception:
		print('Errore query in AgenteDAO')
	finally:
		cur.close()


def deleteAgente(idAgente):
	try:
		con = sql.connect('database.db')
		cur = con.cursor()
		#creazione query
		query = f"DELETE FROM AGENTE WHERE AGENTE.ID ='{idAgente}';"
		cur.execute(query)
		con.commit()
	except Exception:
		print('Errore query in AgenteDAO')
	finally:
		cur.close()

#insert agente
def insertAgente(nome,directory_id, colore, stato, filtro):
	print('inserisco agente')
	try:
		con = sql.connect('database.db')
		cur = con.cursor()
		#creazione query
		query = f"INSERT INTO AGENTE (NOME, DIRECTORY_ID, COLORE,STATO,FILTRO) VALUES ('{nome}', '{directory_id}', '{colore}', '{stato}', '{filtro}');"
		cur.execute(query)
		con.commit()
	except Exception:
		print('Errore query in AgenteDAO')
	finally:
		cur.close()

def listaAgenti():
	print('lista di tutte le directory')
	listaAgenti=[]
	con = sql.connect('database.db')
	cur = con.cursor()
	query = f"SELECT * FROM AGENTE;"
	cur.execute(query)
	result = cur.fetchall()
	if not result: #Risultato vuoto
		print('Nessun agente presente')
		cur.close()
		return listaAgenti
	else:
		print('Mostro lista utenti')
		print(result)
		print('-------')
		for row in result:
			u = Agente(row[0],row[1],row[2],row[3],row[4],row[5])
			listaAgenti.append(u)

	cur.close()
	return listaAgenti


def listaAgentiDir(directory_id):
	print('mostra agenti di una directory')
	listaAgenti = []
	con = sql.connect('database.db')
	cur = con.cursor()
	query = f"SELECT * FROM AGENTE WHERE DIRECTORY_ID='{directory_id}';"
	cur.execute(query)
	print(query)
	result = cur.fetchall()
	if not result:
		print('Nessun agente trovata')
		cur.close()
		return listaAgente
	else:
		print('mostro lista agenti')
		for row in result:
			
			u = Agente(row[0],row[2],row[1],row[3],row[4],row[5])
			listaAgenti.append(u)

	cur.close()
	return listaAgenti
