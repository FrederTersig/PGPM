#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import justpy as jp
import sys

from Model.Agente import Agente

from Template.icons.iconList import startIcon
from Template.icons.iconList import filtroIcon
from Template.icons.iconList import configIcon
from Template.icons.iconList import backendIcon
from Template.icons.iconList import gestioneUtenteIcon
from Template.icons.iconList import gestioneRunIcon
from Template.icons.iconList import gestioneDirectoryIcon
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

def BackendAgenteView(lista,cancellaEle,s):
	wp = jp.WebPage()
	wp.body_style='overflow:hidden'
	mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')   
	####### -------> Pulsantiera Sinistra
	subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')
	#- icona per il tasto del menu start -#
	#initButtonNav = jp.Div(a=subNavDiv, classes=buttonClasses)
	initButtonNav = jp.A(href='/start/', a=subNavDiv, classes=buttonClasses, inner_html=startIcon())
	#- icona per il tasto del menu filter -# -- 
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
	jp.P(a=spanTitleFrame, classes='text-center font-black text-3xl subpixel-antialiased text-white', text='Gestione Agente')
	#Parte centrale del pannello backend                                            
	logFrameDiv = jp.Div(a=subFrameDiv,style=f'height:80%; width:100%;', classes='block divide-y divide-white divide-opacity-25 w-full bg-blue-900 space-y-2 overflow-y-scroll p-2 border-2 border-white rounded-md')
	#for agente in lista:
	#	agenteDiv = jp.Div(a=logFrameDiv, classes='subpixel-antialiased text-white break-words', text=f" ID: {agente.getId()} NOME: {agente.getNome()} DIRECTORY_ID: {agente.getDirectory_id()} COLORE: {agente.getColore()} STATO: {agente.getStato()} FILTRO: {agente.getFiltro()} ")
	#	jp.Div(a=agenteDiv,click=cancellaEle, idAgente={agente.getId()}, classes=buttonClasses+ ' inline-block', text='Cancella')

	#### INIZIO TABELLA
	tableAgente = jp.Table(a=logFrameDiv, classes='table-fixed text-white w-full text-center')
	tableAgenteHead = jp.Thead(a=tableAgente)
	tableAgenteRowMain = jp.Tr(a=tableAgenteHead, classes='bg-gray-100 bg-opacity-50')
	tableAgenteHID = jp.Th(a=tableAgenteRowMain, text='ID')
	tableAgenteHNome = jp.Th(a=tableAgenteRowMain, text='Nome')
	tableAgenteHDi = jp.Th(a=tableAgenteRowMain, text='directory_id')
	tableAgenteHColore= jp.Th(a=tableAgenteRowMain, text='colore')
	tableAgenteHStato =	jp.Th(a=tableAgenteRowMain, text='stato')
	tableAgenteHFiltro = jp.Th(a=tableAgenteRowMain, text='filtro')
	tableAgenteAzioni = jp.Th(a=tableAgenteRowMain, text='cancella')

	tableAgenteBody = jp.Tbody(a=tableAgente)
	for agente in lista:
		tB_Row = jp.Tr(a=tableAgenteBody, classes='border-b-4 border-white border-opacity-25')
		tB_ID = jp.Td(a=tB_Row, text=f'{agente.getId()}')
		tb_Nome = jp.Td(a=tB_Row, text=f'{agente.getNome()}')
		tB_DirID = jp.Td(a=tB_Row, text=f'{agente.getDirectory_id()} ')
		tB_Colore = jp.Td(a=tB_Row, text=f'{agente.getColore()}')
		tB_Stato = jp.Td(a=tB_Row, text=f'{agente.getStato()} ')
		tB_Filtro = jp.Td(a=tB_Row, text=f'{agente.getFiltro()} ')
		tB_Delete = jp.Td(a=tB_Row, classes='flex items-center')
		buttonCancella = jp.Button(a=tB_Delete, classes='block text-center rounded w-20 h-8 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800', click=cancellaEle, idAgente={agente.getId()}, text='Cancella')
	#Spiegazione da inserire

	####### -------> Fine Parte Centrale

		
	return wp