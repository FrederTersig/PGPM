#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

import justpy as jp
import Screens as scr

#Nel main bisogna gestire le varie route attivate dagli eventi dei bottoni nelle screen. 
#Oltre ad impostare la route, bisognerà gestire gli eventi continui.


### Inizio
print('Inizio del programma')

screen = scr.Screen() #Da questa variabile chiamo ogni schermata
#screen.debugScreen() -> per chiamare funzioni all'interno della classe Screen in Screens
#creaLog = screen.logScreen #Richiamo il metodo di creazione del LogScreen
#creaStart = screen.startScreen 
#creaFilter = screen.filterScreen
#creaConfig = screen.configScreen


jp.Route('/start',screen.startScreen)
jp.Route('/filter',screen.filterScreen)
jp.Route('/log',screen.logScreen)
#jp.Route('/config', screen.configScreen)

jp.justpy(screen.startScreen) #la pagina iniziale è quella di start, ma potrebbe essere cambiata
print('fine del programma')
###Fine



