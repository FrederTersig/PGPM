#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import os
import sys
import justpy as jp

from Template.icons.iconList import logIcon
from Template.icons.iconList import configIcon
from Template.icons.iconList import backendIcon
from Template.icons.iconList import startRunIcon
from Template.icons.iconList import editorAgenteIcon
from Template.icons.iconList import disattivaStatoIcon
from Template.icons.iconList import attivaStatoIcon
from Template.icons.iconList import cancellaAgenteIcon
from Template.icons.iconList import filtroIcon
from Template.icons.iconList import profileIcon

coloreAgente = 'background-color:'
agentiClasses = 'inline-block truncate text-center dis rounded w-48 h-20 m-2 bg-[#333333] border-white border text-white'
agentiOnMouseOver = 'inline-block truncate text-center rounded w-48 h-20 m-2 bg-[#FFFFFF] text-black border-black border container'
buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'


def StartView(agEntra,agEsce,startRun,addAgenteEvent,sessione):
	wp = jp.WebPage()
	wp.body_style='overflow:hidden'
	mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')
	####### -------> Pulsantiera Sinistra
	subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')
	#- icona per il tasto del menu start -# IN QUESTO CASO, QUESTO BOTTONE E' DISABLED
	#initButtonNav = jp.Button(a=subNavDiv, classes=buttonClasses)
	#- icona per il tasto del menu log -#
	#logButtonNav = jp.A(href='/log/', a=subNavDiv, classes=buttonClasses, inner_html=logIcon())
	filterButton = jp.A(href='/filter/', a=subNavDiv, classes=buttonClasses, inner_html=filtroIcon())
	#logButtonNav = jp.Button(a=subNavDiv, classes=buttonClasses)
	#- icona per il tasto di configurazione -#
	configButtonNav = jp.A(href='/config/', a=subNavDiv, classes=buttonClasses, inner_html=configIcon())
	if 'logged_in' in sessione and sessione['logged_in']:
		profileButtonNav = jp.A(href='/profile/',a=subNavDiv, classes=buttonClasses, inner_html=profileIcon())
		#if sessione['utente'][4] == 1:
		if 'utente' in sessione and sessione['utente'][4] ==1:
			#- icona per il tasto di Backend -# VISTO SOLO DA ADMIN
			backendButtonNav = jp.A(href='/backend/', a=subNavDiv, classes=buttonClasses, inner_html=backendIcon())
			####### -------> Fine Pulsantiera Sinistra


	####### -------> Parte Centrale: Log
	#Frame dei bottoni
	frameDiv = jp.Div(a=mainDiv, classes='inline-block w-full h-full overflow-hidden')
	subFrameDiv = jp.Div(a=frameDiv, classes='mt-2 h-full space-y-4')
	#Parte superiore: Titolo
	titleFrameDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full pt-3')
	spanTitleFrame = jp.Span(a=titleFrameDiv, classes='align-middle')
	jp.P(a=spanTitleFrame, classes='text-center font-black text-3xl subpixel-antialiased text-white', text='Schermata di Start')
	#Parte centrale: Lista degli agenti     
	#print('Agenti nel path?')
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
	agentsFrameDiv = jp.Div(a=subFrameDiv,style=f'height:80%; width:100%;', classes='block w-full bg-blue-900 overflow-y-scroll p-2 border-2 border-white rounded-md flex flex-wrap justify-center content-start')

	print('-------------------')

	if 'logged_in' in sessione and sessione['logged_in']:
		if 'agenti' in sessione:
			#print('AGENTI IN SESSIONE!!!!')
			for agente in sessione['agenti']:
				colore = sessione['agenti'][agente][0]
				stato = sessione['agenti'][agente][1]
				filtro = sessione['agenti'][agente][2]
				
				stileColore = 'background-color: ' +colore+';'
				if stato == 0:
					x = jp.Button(a=agentsFrameDiv,style=stileColore, classes=agentiClasses+' opacity-50', text=agente, mouseenter=agEntra, mouseleave=agEsce, chiave=agente)
				else:
					x = jp.Button(a=agentsFrameDiv,style=stileColore, classes=agentiClasses, text=agente, mouseenter=agEntra, mouseleave=agEsce, chiave=agente)
		else:
			noAgenti = jp.P(a=agentsFrameDiv,text='Inserisci un Path nella schermata di configurazione!', classes='text-white font-black')
	else:
		noLog = jp.P(a=agentsFrameDiv,text='Devi loggarti prima di poter gestire gli agenti!', classes='text-white font-black')
	#Pulsantiera delle azioni del log
	actionStartDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full')
	bottoniStartDiv = jp.Div(a=actionStartDiv, classes='block flex justify-around')
	if sessione['logged_in'] and 'path' in sessione:
		addAgenteForm = jp.Form(a=bottoniStartDiv, classes='')
		nuovoAgenteInput = jp.Input(type='text',a=addAgenteForm, name='nuovoAgente', id='nuovoAgente', placeholder='Nome Nuovo Agente', classes='inline-block')
		submitAgente = jp.Input(type='submit',value='Aggiungi Agente', a=addAgenteForm, classes='inline-block '+actionButtonClasses)
		addAgenteForm.on('submit', addAgenteEvent)
	#Eventuale altra fila di bottoni
	####### -------> Fine Parte Centrale: Log
	####### -------> Parte Destra: Tasto Filtro
	#Menu Destro (Tasto di 'partenza')
	dxButtonsDiv = jp.Div(a=mainDiv,classes='h-64 inline-block w-22') #Aumento la width così da sistemare al meglio la posizione dei bottoni
	#Bottone destro
	powerOnButton = jp.Div(a=dxButtonsDiv, classes=buttonClasses, click=startRun, inner_html=startRunIcon())
	####### -------> Fine Parte Destra: Tasto Filtro
	return wp


#def cambioColore(elemento, stringa):
#	print('cambio colore elemento -> stringa indica il tipo di colore')

def ShowStop(elemento, onClickStop):
	print('showStop')
	#for element in elemento.components:
	#	print(element)
	#	elemento.components.remove(element)


	elemento.remove(inner_html)
	
	elemento.inner_html=disattivaStatoIcon()

	elemento.remove_event('click')
	elemento.on('click', onClickStop)


	print('fine creazione path')

def ShowPlay(elemento, onClickPlay):
	print('showPlay')
	#for element in elemento.components:
	#	#print(element)
	#	elemento.components.remove(element)
	elemento.remove(inner_html)

	
	elemento.inner_html=attivaStatoIcon()
	elemento.remove_event('click')
		
	elemento.on('click',onClickPlay)
	#Terzo Step: Inserisco l'icona di STOP
	print('fine creazione path')


def ShowMenuAgente(elemento,listaAgenti, onIcona, leaveIcona, onClickStop, onClickPlay,onDeleteAgente):
	#Quando il cursore entra nel bottone, vengono visualizzate le due icone inerenti a quel determinato agente
	#Entra nel bottone
	#print('mouse entra in bottone; Eventi del bottone: ', elemento.events)
	#print(msg.target.has_event_function('mouseleave'))
	#print(msg.target.chiave)
	chiave = elemento.chiave
	print("----- ShowMenuAgente--", chiave)

	elemento.text=''
	
	
	tastoDiv = jp.Div(a=elemento, classes='block flex justify-evenly items-center py-3')
	# Play sulla Sinistra
		
	attivo = listaAgenti[chiave][1]
	
	if attivo == 1:
		divPlay = jp.Div(a=tastoDiv, classes='flex-auto', click=onClickStop, chiave=chiave,inner_html=disattivaStatoIcon())
		modAgentiClass=agentiOnMouseOver
	else:
		divPlay = jp.Div(a=tastoDiv, classes='flex-auto', click=onClickPlay, chiave=chiave, inner_html=attivaStatoIcon())
		modAgentiClass=agentiOnMouseOver+' opacity-50'
			
	divElimina = jp.Div(a=tastoDiv, classes='flex-auto',click=onDeleteAgente, chiave=chiave,inner_html=cancellaAgenteIcon())

	elemento.classes=modAgentiClass

	# Code sulla destra

	linkAgente = '/editor/'+elemento.chiave
	print('linkAgente ----->', linkAgente)
	#divCode = jp.Div(a=tastoDiv, classes='flex-auto')
	divCode = jp.A(a=tastoDiv, href=linkAgente, classes='flex-auto', inner_html=editorAgenteIcon())

def ShowButtonAgente(elemento, agEntra, agEsce):
	for element in elemento.components:
		#print(element)
		elemento.components.remove(element)
		
	elemento.classes=agentiClasses
	elemento.mouseenter=agEntra
	elemento.mouseleave=agEsce
	elemento.text=elemento.chiave



