#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import justpy as jp
import sys

from Model.Utente import Utente

from Template.icons.iconList import startIcon
from Template.icons.iconList import filtroIcon
from Template.icons.iconList import configIcon
from Template.icons.iconList import backendIcon
from Template.icons.iconList import gestioneRunIcon
from Template.icons.iconList import gestioneDirectoryIcon
from Template.icons.iconList import gestioneAgenteIcon
from Template.icons.iconList import profileIcon

#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'
buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
#Codice della grafica della schermata di BACKEND

############################################

def BackendUtenteView(listaUtenti,cancellaEle,cambioRuoloEle,s):
	wp = jp.WebPage()
	wp.body_style='overflow:hidden'
	mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')   
	####### -------> Pulsantiera Sinistra
	subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')
	#- icona per il tasto del menu start -#
	#initButtonNav = jp.Div(a=subNavDiv, classes=buttonClasses)
	initButtonNav = jp.A(href='/start/', a=subNavDiv, classes=buttonClasses, inner_html=startIcon())
	#- icona per il tasto del menu log -# -- 
	filterButton = jp.A(href='/filter/', a=subNavDiv, classes=buttonClasses, inner_html=filtroIcon())
	#- icona per il tasto di configurazione -#
	configButtonNav = jp.A(href='/config/', a=subNavDiv, classes=buttonClasses, inner_html=configIcon())
	#- icona per il tasto di Backend -# VISTO SOLO DA ADMIN
	if s['logged_in']:
		profileButtonNav = jp.A(href='/profile/',a=subNavDiv, classes=buttonClasses, inner_html=profileIcon())
		if s['utente'][4] == 1:
			backendButtonNav = jp.A(href='/backend/', a=subNavDiv, classes=buttonClasses, inner_html=backendIcon())
	####### -------> Fine Pulsantiera Sinistra


	####### -------> Parte Centrale: Pannello Backend Spiegazione
	#Frame dei bottoni
	frameDiv = jp.Div(a=mainDiv, classes='inline-block w-full h-full overflow-hidden')
	subFrameDiv = jp.Div(a=frameDiv, classes='mt-2 h-full space-y-4')
	#Parte superiore: Titolo
	titleFrameDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full pt-4')
	spanTitleFrame = jp.Span(a=titleFrameDiv, classes='align-middle')
	jp.P(a=spanTitleFrame, classes='text-center font-black text-3xl subpixel-antialiased text-white', text='Gestione Utente')
	#Parte centrale del pannello backend                                            
	logFrameDiv = jp.Div(a=subFrameDiv,style=f'height:80%; width:100%;', classes='block divide-y divide-white divide-opacity-25 w-full bg-blue-900 space-y-2 overflow-y-scroll p-2 border-2 border-white rounded-md')
	###################
	#### INIZIO TABELLA
	tableUtente = jp.Table(a=logFrameDiv, classes='table-fixed text-white w-full text-center')
	tableUtenteHead = jp.Thead(a=tableUtente)
	tableUtenteRowMain = jp.Tr(a=tableUtenteHead, classes='bg-gray-100 bg-opacity-50')
	tableUtenteHID = jp.Th(a=tableUtenteRowMain, text='ID')
	tableUtenteHNome = jp.Th(a=tableUtenteRowMain, text='Nome')
	tableUtenteHEmail = jp.Th(a=tableUtenteRowMain, text='Email')
	tableUtenteHPassword = jp.Th(a=tableUtenteRowMain, text='Password')
	tableUtenteHRuolo = jp.Th(a=tableUtenteRowMain, text='Ruolo')
	tableUtenteHAzioni = jp.Th(a=tableUtenteRowMain, text='Azioni')

	tableUtenteBody = jp.Tbody(a=tableUtente)
	for utente in listaUtenti:
		tB_Row = jp.Tr(a=tableUtenteBody, classes='border-b-4 border-white border-opacity-25')
		tB_ID = jp.Td(a=tB_Row, text=f'{utente.getId()}')
		tB_Nome = jp.Td(a=tB_Row, text=f'{utente.getNome()} ')
		tB_Email = jp.Td(a=tB_Row, text=f'{utente.getEmail()}')
		tB_Pass = jp.Td(a=tB_Row, text=f'{utente.getPassword()}')
		tB_Ruolo = jp.Td(a=tB_Row, text=f'{utente.getRuolo()} ')
		tB_Azioni = jp.Td(a=tB_Row, classes='flex items-center relative')
		divAzioneCancella = jp.Div(a=tB_Azioni)
		buttonCancella = jp.Button(a=divAzioneCancella, classes='block text-center rounded w-20 h-8 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800', click=cancellaEle, idUtente={utente.getId()}, text='Cancella')
		divAzioneCambioRuolo = jp.Div(a=tB_Azioni, classes='absolute right-0')
		if utente.getRuolo() == 0:
			buttonCambioRuolo = jp.Button(a=divAzioneCambioRuolo, classes='block text-center rounded w-20 h-8 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800', click=cambioRuoloEle, idUtente={utente.getId()}, ruolo='1', text='Promuovi')
		else:
			buttonCambioRuolo = jp.Button(a=divAzioneCambioRuolo, classes='block text-center rounded w-20 h-8 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800', click=cambioRuoloEle, idUtente={utente.getId()}, ruolo='0', text='Retrocedi')
	#for utente in listaUtenti:
	#	utenteDiv = jp.Div(a=logFrameDiv, classes='subpixel-antialiased text-white break-words', text=f" ID: {utente.getId()} NOME: {utente.getNome()} EMAIL: {utente.getEmail()} PASSWORD: {utente.getPassword()} RUOLO: {utente.getRuolo()}")
	#	jp.Div(a=utenteDiv,click=cancellaEle, idUtente={utente.getId()}, classes=buttonClasses+ ' inline-block', text='Cancella')
	####### -------> Fine Parte Centrale

		
	return wp