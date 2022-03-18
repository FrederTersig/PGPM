#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

import sys
sys.path.append('Scrivania/PGPM')

import justpy as jp
import Screens as scr
print('Inizio del programma')


creaStart = scr.StartScreen()
creaLog = scr.LogScreen()
creaFilter = scr.FilterScreen()
creaEditor = scr.EditorAgente()
creaConfig = scr.ConfigScreen()
creaProfile = scr.ProfileScreen()
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
jp.Route('/profile/', creaProfile.profileScreen)
jp.Route('/config/newUser/', creaNewUser.newUserController)
jp.Route('/backend/', creaBackend.backendScreen)
jp.Route('/backend/gestioneUtente/', gestioneUtente.backendUtenteScreen)
jp.Route('/backend/gestioneRun/', gestioneRun.backendRunScreen)
jp.Route('/backend/gestioneDirectory/', gestioneDirectory.backendDirectoryScreen)
jp.Route('/backend/gestioneAgente/', gestioneAgente.backendAgenteScreen)

jp.Route('/editor/{name}', creaEditor.editorAgente)



print('inizio con startScreen')

jp.justpy(creaStart.startScreen)
print('Si procede anche qui?')

print('fine del programma')
###Fine

