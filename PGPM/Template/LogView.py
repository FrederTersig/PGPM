#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import os
import sys
import justpy as jp
import asyncio
from Template.icons.iconList import startIcon
from Template.icons.iconList import startRunIcon
from Template.icons.iconList import logIcon
from Template.icons.iconList import configIcon
from Template.icons.iconList import backendIcon
from Template.icons.iconList import filtroIcon
from Template.icons.iconList import annullaIcon


#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'
buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
#Codice della grafica della schermata di LOG

#Output cercato dalla schermata di log (Usare chiamata con API)
#Variabili output: per ora solo prove
timestamp = 'TimeStamp'
message = 'Message'
nomeAgente = 'Nome Agente'
############################################

def LogView(s,showLog,stopThread):
	wp = jp.WebPage()
	wp.body_style='overflow:hidden'
	mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')
	####### -------> Pulsantiera Sinistra
	wp.subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')

	
	#- icona per il tasto del menu start -#
	#initButtonNav = jp.Div(a=subNavDiv, classes=buttonClasses)
	initButtonNav = jp.Button(click=stopThread, a=wp.subNavDiv, classes=buttonClasses, inner_html=startRunIcon())

	#- icona per il tasto di configurazione -#
	#configButtonNav = jp.A(href='/config/', a=subNavDiv, classes=buttonClasses, inner_html=configIcon())
	#- icona per il tasto di Backend -# VISTO SOLO DA ADMIN
	#if s['logged_in']:
	#	if s['utente'][4] == 1:
	#		backendButtonNav = jp.A(href='/backend/', a=subNavDiv, classes=buttonClasses, inner_html=backendIcon())
	####### -------> Fine Pulsantiera Sinistra

	####### ----> Parte Centrale: Log
	#Frame dei Bottoni
	frameDiv = jp.Div(a=mainDiv, classes='inline-block w-full h-full overflow-hidden')
	subFrameDiv = jp.Div(a=frameDiv, classes='mt-2 h-full space-y-4')
	#Parte superiore: Titolo
	titleFrameDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full pt-3')
	spanTitleFrame = jp.Span(a=titleFrameDiv, classes='align-middle')
	jp.P(a=spanTitleFrame, classes='text-center font-black text-3xl subpixel-antialiased text-white', text='Schermata dei Log')
	### -- > < -- ###
	#Div - Div if
	divShowUt = jp.Div(a=titleFrameDiv, classes='w-full flex justify-between')
	divLeftUt = jp.Div(a=divShowUt, classes='text-left inline-block')
	#if con p
	if 'utente' in s:
		ut_email = s['utente'][2]
		jp.P(a=divLeftUt, classes='m-1 text-white font-black text-left',text='Connesso come: '+ut_email)
	else:
		jp.P(a=divLeftUt, classes='m-1 text-white font-black text-left', text='Visitatore, registrati o fai il login!')
	
	divRightUt = jp.Div(a=divShowUt, classes='text-right inline-block')
	#if con p
	if 'path' in s and 'nome_path' in s:
		pathString = 'Nome del Path:'+s['nome_path']+' - Path Inserito: '+s['path']
		jp.P(a=divRightUt, classes='m-1 text-white font-black text-left',text=pathString)
	else:
		jp.P(a=divRightUt, classes='m-1 text-white font-black text-left', text='Nessun Path Inserito')

	### -- > < -- ###

	#Parte centrale: Lista degli output                                             
	wp.logFrameDiv = jp.Div(delete_flag=False,a=subFrameDiv, id='logFrameDiv',style=f'height:80%; width:100%;', classes='block divide-y divide-white divide-opacity-25 w-full bg-blue-900 space-y-2 overflow-y-scroll p-2 border-2 border-white rounded-md')
	
	#while True:
		
	#	await asyncio.sleep(1)
	#	logFrameDiv.add(jp.P(a=logFrameDiv, classes='subpixel-antialiased text-white break-words'),'prova',p)
	#	await logFrameDiv.update()
	#jp.P(a=logFrameDiv, classes='subpixel-antialiased text-white break-words', text='> '+timestamp+' | '+message+' | '+nomeAgente)
	#Pulsantiera delle azioni del log
	actionLogDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full')
	bottoniLogDiv = jp.Div(a=actionLogDiv, classes='block flex justify-around')
	#exportLogButton = jp.Button(text='Esporta Log', a=bottoniLogDiv, classes=actionButtonClasses)
	#cleanLogButton = jp.Button(text='Pulisci Tutto', a=bottoniLogDiv, classes=actionButtonClasses)
	#Eventuale altra fila di bottoni
	####### -------> Fine Parte Centrale: Log
	####### -------> Parte Destra: Tasto Filtro
	#Menu Destro (Tasto del filtro)
	#filterNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block w-22') #Aumento la width così da sistemare al meglio la posizione dei bottoni
	#filterButton = jp.A(href='/filter/', a=filterNavDiv, classes=buttonClasses, inner_html=filtroIcon())
	####### -------> Fine Parte Destra: Tasto Filtro
	wp.on('page_ready',showLog)
	return wp

def insertButton(elemento):
	rejectButton = jp.A(href='/start', a=elemento, classes=rejectClasses, inner_html=annullaIcon())

def addLog(elemento,testo, colore):
	#print('ADD LOG MOSTRA IL TESTO CHE VIENE MANDATO!!!')
	#print(testo)
	if colore=='alert':
		stileColore = 'background-color: #c51f1f;'
	else:
		stileColore = 'background-color: ' +colore+';'

	log = jp.P(a=elemento,classes='subpixel-antialiased text-white break-words font-black text-lg',style=stileColore ,text=testo)