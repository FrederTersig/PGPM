#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import os
import sys
import justpy as jp

from Template.icons.iconList import annullaIcon
from Template.icons.iconList import disattivaFiltroIcon
from Template.icons.iconList import attivaFiltroIcon
from Template.icons.iconList import configIcon
from Template.icons.iconList import backendIcon
from Template.icons.iconList import startIcon
from Template.icons.iconList import profileIcon

#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block truncate text-center dis rounded w-48 h-20 m-2 bg-[#333333] border-white border text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block truncate text-center rounded w-48 h-20 m-2 bg-[#FFFFFF] text-black border-black border container'
buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'

#Codice della grafica della schermata di LOG
############################################
#Prima di tutto, creo un'istanza della classe Agente



def FilterView(filtroAgEntra, filtroAgEsce,sessione):
	wp = jp.WebPage()
	wp.body_style='overflow:hidden'


	mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')
	####### -------> Pulsantiera Sinistra
	subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')
	#- icona per il tasto del menu start -#
	initButtonNav = jp.A(href='/start/', a=subNavDiv, classes=buttonClasses, inner_html=startIcon())

	#- icona per il tasto di configurazione -#
	configButtonNav = jp.A(href='/config/', a=subNavDiv, classes=buttonClasses, inner_html=configIcon())
	#- icona per il tasto di Backend -# VISTO SOLO DA ADMIN
	if sessione['logged_in']:
		profileButtonNav = jp.A(href='/profile/',a=subNavDiv, classes=buttonClasses, inner_html=profileIcon())
		if sessione['utente'][4] == 1:
			backendButtonNav = jp.A(href='/backend/', a=subNavDiv, classes=buttonClasses, inner_html=backendIcon())
	####### -------> Fine Pulsantiera Sinistra
	####### -------> Parte Centrale: Log
	#Frame dei bottoni
	frameDiv = jp.Div(a=mainDiv, classes='inline-block w-full h-full overflow-hidden')
	subFrameDiv = jp.Div(a=frameDiv, classes='mt-2 h-full space-y-4')
	#Parte superiore: Titolo
	titleFrameDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full pt-3')
	spanTitleFrame = jp.Span(a=titleFrameDiv, classes='align-middle')
	jp.P(a=spanTitleFrame, classes='text-center font-black text-3xl subpixel-antialiased text-white', text='Imposta Filtro')
	### -- > < -- ###
	#Div - Div if
	divShowUt = jp.Div(a=titleFrameDiv, classes='w-full flex justify-between')
	divLeftUt = jp.Div(a=divShowUt, classes='text-left inline-block')
	#if con p
	if 'utente' in sessione:
		ut_email = sessione['utente'][2]
		jp.P(a=divLeftUt, classes='m-1 text-white font-black text-left',text='Connesso come: '+ut_email)
	else:
		jp.P(a=divLeftUt, classes='m-1 text-white font-black text-left', text='Visitatore, registrati o fai il login!')
	
	divRightUt = jp.Div(a=divShowUt, classes='text-right inline-block')
	#if con p
	if 'path' in sessione and 'nome_path' in sessione:
		pathString = 'Nome del Path:'+sessione['nome_path']+' - Path Inserito: '+sessione['path']
		jp.P(a=divRightUt, classes='m-1 text-white font-black text-left',text=pathString)
	else:
		jp.P(a=divRightUt, classes='m-1 text-white font-black text-left', text='Nessun Path Inserito')

	### -- > < -- ###
	#Parte centrale: Lista degli agenti                                           
	agentsFrameDiv = jp.Div(a=subFrameDiv,style=f'height:80%; width:100%;', classes='block w-full bg-blue-900 overflow-y-scroll p-2 border-2 border-white rounded-md flex flex-wrap justify-center content-start')
	#jp.P(a=agentsFrameDiv, classes='subpixel-antialiased text-white break-words', text='> '+timestamp+' | '+message+' | '+nomeAgente)
	# Al posto di questo jp.P, bisogna mettere la lista degli agenti che si trova all'interno della finestra.
	
	if sessione['logged_in']:
		if 'agenti' in sessione:
			for agente in sessione['agenti']:	
				colore = sessione['agenti'][agente][0]
				stato = sessione['agenti'][agente][1]
				filtro = sessione['agenti'][agente][2]
				
				stileColore = 'background-color: ' +colore+';'
				x = jp.Button(a=agentsFrameDiv,style=stileColore, classes=agentiClasses, text=agente, mouseenter=filtroAgEntra, mouseleave=filtroAgEsce, chiave=agente)


	#Pulsantiera delle azioni del log
	actionStartDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full')
	bottoniStartDiv = jp.Div(a=actionStartDiv, classes='block flex justify-around')

	#Eventuale altra fila di bottoni
	####### -------> Fine Parte Centrale: Log
	####### -------> Parte Destra: Tasto Filtro
	#Menu Destro (Tasto di 'partenza')
	dxButtonsDiv = jp.Div(a=mainDiv,classes='h-64 inline-block w-22') #Aumento la width così da sistemare al meglio la posizione dei bottoni
	####### -------> Fine Parte Destra: Tasto Filtro
	return wp

def ShowRimuovi(elemento,onRimuovi):
	print('Mostra il tasto rimuovi togliendo il +')
	for element in elemento.components:
		#print(element)
		elemento.components.remove(element)
	#Secondo Step: Cambio le componenti del SVG
	
		
	elemento.classes='bi bi-dash-circle-fill'
	elemento.remove_event('click')
	elemento.on('click',onRimuovi)
	#Terzo Step: Inserisco l'icona di PIU
	jp.Path(a=elemento, d='M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM4.5 7.5a.5.5 0 0 0 0 1h7a.5.5 0 0 0 0-1h-7z')
	print('fine ShowRimuovi')

def ShowAggiungi(elemento, onAggiungi):
	print('Mostra il tasto aggiungi rimuovendo il -')
	for element in elemento.components:
		elemento.components.remove(element)
		#Secondo Step: Cambio le componenti del SVG

	elemento.classes='bi bi-dash-plus-fill'
	elemento.remove_event('click')
	elemento.on('click',onAggiungi)
	#Terzo Step: Inserisco l'icona di Meno
	jp.Path(a=elemento, d='M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z')

	print('fine ShowAggiungi')

def ShowMenuFiltroAgente(elemento, listaAgenti, onIcona, leaveIcona, onClickRimuovi, onClickAggiungi, cambioColore):
	print('entra in filtro')
	elemento.text=''
	elemento.classes=agentiOnMouseOver

	tastoDiv = jp.Div(a=elemento, classes='block flex justify-evenly items-center py-3')
	# Play sulla Sinitra
	

	print('PROVA::::: --------> MSG')
	filtro = listaAgenti[elemento.chiave][2]

	if filtro == 1:
		#Metti il MENO
		divPlay = jp.Div(a=tastoDiv, click=onClickRimuovi, classes='flex-auto',inner_html=disattivaFiltroIcon(), chiave=elemento.chiave)
			
	else:
		#Metti il PIU
		divPlay = jp.Div(a=tastoDiv,click=onClickAggiungi, classes='flex-auto', inner_html=attivaFiltroIcon(), chiave=elemento.chiave)
			
		# Code sulla destra
	divColor = jp.Div(a=tastoDiv, classes='flex-auto')
	tastoColor = jp.Input(type='color', a=divColor, classes='', style='width: 40px; height: 40px', input=cambioColore, chiave=elemento.chiave)

def ShowButtonFiltroAgente(elemento, filtroAgEntra, filtroAgEsce):
	for element in elemento.components:
		#print(element)
		elemento.components.remove(element)
		
	elemento.classes=agentiClasses
	elemento.mouseenter=filtroAgEntra
	elemento.mouseleave=filtroAgEsce
	elemento.text=elemento.chiave
	#print('USCITO')