#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import justpy as jp
import sys


from Template.icons.iconList import startIcon
from Template.icons.iconList import filtroIcon
from Template.icons.iconList import configIcon
from Template.icons.iconList import backendIcon
from Template.icons.iconList import gestioneUtenteIcon
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

#PATH

############################################

def BackendView(s):
	print('BACKENDSCREEN')
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
	profileButtonNav = jp.A(href='/profile/',a=subNavDiv, classes=buttonClasses, inner_html=profileIcon())
	#if s['logged_in']:
	#	if s['utente'][4] == 1:
	#		backendButtonNav = jp.A(href='/backend/', a=subNavDiv, classes=buttonClasses, inner_html=backendIcon())
	####### -------> Fine Pulsantiera Sinistra

	####### -------> Parte Centrale: Pannello Backend Spiegazione
	#Frame dei bottoni
	frameDiv = jp.Div(a=mainDiv, classes='inline-block w-full h-full overflow-hidden')
	subFrameDiv = jp.Div(a=frameDiv, classes='mt-2 h-full space-y-4')
	#Parte superiore: Titolo
	titleFrameDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full pt-3')
	spanTitleFrame = jp.Span(a=titleFrameDiv, classes='align-middle')
	jp.P(a=spanTitleFrame, classes='text-center font-black text-3xl subpixel-antialiased text-white', text='Schermata di Backend')
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
	#Parte centrale del pannello backend                                            
	logFrameDiv = jp.Div(a=subFrameDiv,style=f'height:80%; width:100%;', classes='w-full bg-blue-900 p-2 border-2 border-white rounded-mdr')
	backendMenuDiv = jp.Div(a=logFrameDiv, classes='w-full divide-y divide-white divide-dashed divide-opacity-25 grid grid-rows-6 grid-flow-col justify-center my-16 align-middle')
	
	divCentroUtente = jp.Div(a=backendMenuDiv, classes='flex items-center')
	backendUtenteButton = jp.A(inner_html=gestioneUtenteIcon(), href='/backend/gestioneUtente/', a=divCentroUtente, classes=buttonClasses)
	jp.P(a=divCentroUtente,classes='inline-block font-black text-white text-2xl', text='Gestione Utenza')

	divCentroRun = jp.Div(a=backendMenuDiv, classes='flex items-center')
	backendRunButton = jp.A(inner_html=gestioneRunIcon(), href='/backend/gestioneRun/', a=divCentroRun, classes=buttonClasses)
	jp.P(a=divCentroRun,classes='inline-block font-black text-white text-2xl', text='Gestione Run')

	divCentroDirectory = jp.Div(a=backendMenuDiv, classes='flex items-center')
	backendDirectoryButton = jp.A(inner_html=gestioneDirectoryIcon(), href='/backend/gestioneDirectory/', a=divCentroDirectory, classes=buttonClasses)
	jp.P(a=divCentroDirectory,classes='inline-block font-black text-white text-2xl', text='Gestione Directory')

	divCentroAgente = jp.Div(a=backendMenuDiv, classes='flex items-center')
	backendAgenteButton = jp.A(inner_html=gestioneAgenteIcon(), href='/backend/gestioneAgente/', a=divCentroAgente, classes=buttonClasses)
	jp.P(a=divCentroAgente,classes='inline-block font-black text-white text-2xl', text='Gestione Agente')

	####### -------> Fine Parte Centrale


	####### -------> Parte Destra: Tasti di gestione del db
	#Menu Destro (Tasto del filtro)
	#backendNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block w-22') #Aumento la width così da sistemare al meglio la posizione dei bottoni

	#backendUtenteButton = jp.A(inner_html=gestioneUtenteIcon(), href='/backend/gestioneUtente/', a=backendNavDiv, classes=buttonClasses)

	#backendRunButton = jp.A(inner_html=gestioneRunIcon(), href='/backend/gestioneRun/', a=backendNavDiv, classes=buttonClasses)

	#backendDirectoryButton = jp.A(inner_html=gestioneDirectoryIcon(), href='/backend/gestioneDirectory/', a=backendNavDiv, classes=buttonClasses)

	#backendAgenteButton = jp.A(inner_html=gestioneAgenteIcon(), href='/backend/gestioneAgente/', a=backendNavDiv, classes=buttonClasses)

	####### -------> Fine Parte Destra
		
	return wp