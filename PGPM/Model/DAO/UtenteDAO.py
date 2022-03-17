#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
from Model.Utente import Utente
import sqlite3 as sql


#funzione di Debug
#def check_connection(self, con):
#		try:
#			con.cursor()
#			return True
#		except Exception as ex:
#			return False




#class UtenteDao:


#Lista di query che bisogna scrivere per l'Utente
#	def utenteDAO(self):
#		pass
#Autenticazione al sito - Login


def validazione(email, password):
	#Connessione al DB
	#email = 'Gianlupo@gmail.com'
	#password = 'password'
	con = sql.connect('database.db')
	cur = con.cursor()
	#Creazione Query
	query = f"SELECT * from UTENTE WHERE EMAIL = '{email}' AND PASSWORD = '{password}';"
	cur.execute(query)
	utente = cur.fetchone()
	#print('utente--- ', utente)
	#print(type(utente))
	if utente is None: #Un risultato vuoto è FALSE
		print('Login Fallito!')
		return None
	else:
		print('Login Riuscito! Benvenuto!!', type(utente))
		return utente



def listaUtente():
	print('Mostra tutti gli utenti')
	listaUtenti = []
	con = sql.connect('database.db')
	cur = con.cursor()
	query = f"SELECT ID,NOME, EMAIL, PASSWORD, RUOLO FROM UTENTE;"
	cur.execute(query)
	print(query)
	result = cur.fetchall()
	if not result: #Risultato vuoto
		print('Nessun utente presente')
		cur.close()
		return listaUtenti
	else:
		print('Mostro lista utenti')
		print(result)
		print('-------')
		for row in result:
			u = Utente(row[0],row[1],row[2],row[3],row[4])
			listaUtenti.append(u)
			#row[0]#nome
			#row[1]#email
			#row[2]#password
			#row[3]#ruolo


	cur.close()
	return listaUtenti

#Dato nome, seleziona un determinato utente

def searchUtente(nome):
	print('Ricerca utente per nome')
	con = sql.connect('database.db')
	cur = con.cursor()
	#creazione query
	query = f"SELECT ID FROM UTENTE WHERE UTENTE.EMAIL ='{email}';"
	cur.execute(query)
	if not cur.fetchone(): # fetchall?
		print('NON riuscito')
	else:
		print('riuscito')
	print('Restituisci utente')

#Update dell'utente --> Modifica informazioni dell'account
def updateUtente(idUtente, nome, password, email, ruolo): 
	print('Modifica le informazioni utente')
	con = sql.connect('database.db')
	cur = con.cursor()
	#creazione query
	query = f"UPDATE UTENTE SET NOME='{nome}', PASSWORD='{password}', EMAIL='{email}', RUOLO='{ruolo}' WHERE UTENTE.ID ='{idUtente}';"
	cur.execute(query)
	con.commit()
	cur.close()
	print('ritorna TRUE se sei riuscito, false altrimenti')

def updateRuolo(idUtente,ruolo):
	print('Modifica le informazioni utente')
	print('Ruolo --> ', ruolo, ' ! idUtente - ' , idUtente)
	con = sql.connect('database.db')
	cur = con.cursor()
	#creazione query
	query = f"UPDATE UTENTE SET RUOLO='{ruolo}' WHERE UTENTE.ID ='{idUtente}';"
	cur.execute(query)
	con.commit()
	cur.close()
	print('ritorna TRUE se sei riuscito, false altrimenti')

def updateEmail(idUtente,email):
	print('Modifica le informazioni utente')
	con = sql.connect('database.db')
	cur = con.cursor()
	#creazione query
	query = f"UPDATE UTENTE SET EMAIL='{email}' WHERE UTENTE.ID ='{idUtente}';"
	cur.execute(query)
	con.commit()
	cur.close()
	print('ritorna TRUE se sei riuscito, false altrimenti')

def checkPassword(idUtente):
	print('check della password')
	con = sql.connect('database.db')
	cur = con.cursor()
	query = f"SELECT PASSWORD FROM UTENTE WHERE UTENTE.ID ='{idUtente}';"
	cur.execute(query)
	result = cur.fetchone()
	if not result:
		print('non riuscito')
	else:
		print('riuscito')
	return result[0]

def updatePassword(idUtente,password):
	print('Modifica le informazioni utente')
	con = sql.connect('database.db')
	cur = con.cursor()
	#creazione query
	query = f"UPDATE UTENTE SET PASSWORD='{password}' WHERE UTENTE.ID ='{idUtente}';"
	cur.execute(query)
	con.commit()
	cur.close()
	print('ritorna TRUE se sei riuscito, false altrimenti')

#insert utente
def insertUtente(nome,email,password,ruolo):
	print('inserisco utente')
	con = sql.connect('database.db')
	cur = con.cursor()
	#creazione query
	query = f"INSERT INTO UTENTE (NOME, EMAIL, PASSWORD,RUOLO) VALUES ('{nome}', '{email}', '{password}', 0);"
	cur.execute(query)
	con.commit()
	cur.close()


#Delete dell'utente --> Cancellazione account
def deleteUtente(idUtente):
	print('Cancella un determinato account')
	con = sql.connect('database.db')
	cur = con.cursor()
	#creazione query
	query = f"DELETE FROM UTENTE WHERE UTENTE.ID ='{idUtente}';"
	print('fetch per vedere se riesce o meno')
	cur.execute(query)
	con.commit()
	cur.close()

#Update del ruolo dell'utente

