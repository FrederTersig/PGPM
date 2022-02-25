#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

import sys
sys.path.append('Scrivania/PGPM')

import justpy as jp
import Screens as scr
#from Screens import StartScreen
#from Screens import FilterScreen
#from Screens import LogScreen
#from Screens import EditorAgente
#from Engine import Agente #Voglio solo una funzione

#from Screens.StartScreen import StartScreen
#from Screens.LogScreen import LogScreen
#from Screens.FilterScreen import FilterScreen

#from Screens.StartScreen import a

#Se vuoi importare un file presente in un'altra cartella all'interno della cartella che ha il main, devi fare così come scritto
#from (Cartella presente nella stessa cartella del main).(Sottocartella della cartella) import (nome del file da importare)

#Nel main bisogna gestire le varie route attivate dagli eventi dei bottoni nelle screen. 
#Oltre ad impostare la route, bisognerà gestire gli eventi continui.


### Inizio
print('Inizio del programma')
#a.prova()


#creaStart = StartScreen.StartScreen()
#creaLog = LogScreen.LogScreen()
#creaFilter = FilterScreen.FilterScreen()
#mostraEditor = EditorAgente.EditorAgente()

creaStart = scr.StartScreen()
creaLog = scr.LogScreen()
creaFilter = scr.FilterScreen()
creaEditor = scr.EditorAgente()
creaConfig = scr.ConfigScreen()
creaNewUser = scr.NewUserController()

creaBackend = scr.BackendScreen()
gestioneUtente = scr.BackendUtenteScreen()
gestioneRun = scr.BackendRunScreen()
gestioneDirectory = scr.BackendDirectoryScreen()
gestioneAgente = scr.BackendAgenteScreen()


print('Procedo con le route')
#jp.Route('/start',creaStart.startScreen)
#jp.Route('/filter',creaFilter.filterScreen)
#jp.Route('/log',creaLog.logScreen)
#jp.Route('/editor/{name}', mostraEditor.editorAgente)

jp.Route('/start/', creaStart.startScreen)
jp.Route('/log/', creaLog.logScreen)
jp.Route('/filter/', creaFilter.filterScreen)
jp.Route('/config/', creaConfig.configScreen)
jp.Route('/config/newUser/', creaNewUser.newUserController)
jp.Route('/backend/', creaBackend.backendScreen)
jp.Route('/backend/gestioneUtente/', gestioneUtente.backendUtenteScreen)
jp.Route('/backend/gestioneRun/', gestioneRun.backendRunScreen)
jp.Route('/backend/gestioneDirectory/', gestioneDirectory.backendDirectoryScreen)
jp.Route('/backend/gestioneAgente/', gestioneAgente.backendAgenteScreen)

jp.Route('/editor/{name}', creaEditor.editorAgente)



print('inizio con startScreen')
#jp.justpy(creaLog.logScreen)
#jp.justpy(creaStart.startScreen)
jp.justpy(creaStart.startScreen)
print('Si procede anche qui?')
#jp.Route('/start',screen.startScreen)
#jp.Route('/filter',screen.filterScreen)
#jp.Route('/log',screen.logScreen)
#jp.Route('/config', screen.configScreen)

#jp.justpy(screen.startScreen) #la pagina iniziale è quella di start, ma potrebbe essere cambiata
print('fine del programma')
###Fine
