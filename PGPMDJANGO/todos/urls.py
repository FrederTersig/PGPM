# todos/urls.py

from django.urls import path

#Schermate Principali
from .views import startScreen
from .views import logScreen
from .views import filterScreen
from .views import configScreen
from .views import backendScreen

#Schermate del Backend
from .views import backendUtenteScreen
from .views import backendRunScreen
from .views import backendDirectoryScreen
from .views import backendAgenteScreen

#Schermate dipendenti dalla StartScreen
from .views import editorScreen
from .views import buttonAgente
from .views import buttonAgenteBack
from .views import setStato
from .views import salvaCodice
from .views import deleteAgente
from .views import startRun
from .views import addAgente

#Schermata dipendente dal LogScreen
from .views import showLog
from .views import stopLog

#Schermate dipendenti dalla FilterScreen
from .views import filtroButtonAgente
from .views import filtroButtonAgenteBack
from .views import editColor
from .views import setFilter

#Schermate dipendenti dalla configScreen
from .views import login
from .views import logout
from .views import savePath
from .views import newUser
from .views import sendNewUser
from .views import scegliPath
from .views import cancellaRunScelta

#funzioni dipendenti da backendUtenteScreen
from .views import cancellaUtente

from .views import cancellaRun

from .views import cancellaDirectory

from .views import cancellaAgenteDB


###

urlpatterns = [
    #Principali
    path('',startScreen,name='startScreen'),
    path('start/', startScreen, name='startScreen'),
    path('log/', logScreen, name='logScreen'),
    path('filter/',filterScreen, name='filterScreen'),
    path('backend/', backendScreen, name='backendScreen'),
    path('config/', configScreen, name='configScreen'),

    #Schermate di Backend
    path('backend/gestioneUtente', backendUtenteScreen, name='backendUtenteScreen'),
    path('backend/gestioneRun', backendRunScreen, name='backendRunScreen'),
    path('backend/gestioneDirectory', backendDirectoryScreen, name='backendDirectoryScreen'),
    path('backend/gestioneAgente', backendAgenteScreen, name='backendAgenteScreen'),

    #Dipendenti da StartScreen
    path('start/<str:nomeAgente>/', editorScreen, name='editorScreen'),
    path('buttonAgente/', buttonAgente, name='buttonAgente'),
    path('buttonAgenteBack/',buttonAgenteBack, name='buttonAgenteBack'),
    path('setStato/', setStato, name='setStato'),
    path('start/<str:nomeAgente>/salvaCodice/', salvaCodice, name='salvaCodice'),
    path('deleteAgente/', deleteAgente, name='deleteAgente'),
    path('startRun/', startRun, name='startRun'),
    path('addAgente/', addAgente, name='addAgente'),

    #Dipendenti dal LogScreen
    path('updateLog/', showLog, name='showLog'),
    path('stopLog/', stopLog, name='stopLog'),

    #Diupendenti da FilterScreen
    path('filtroButtonAgente/', filtroButtonAgente, name='filtroButtonAgente'),
    path('filtroButtonAgenteBack/', filtroButtonAgenteBack, name='filtroButtonAgenteBack'),
    path('editColor/', editColor, name='editColor'),
    path('setFilter/', setFilter, name='setFilter'),

    #Dipendendi da configScreen
    path('config/login/', login, name='login'),
    path('config/logout/', logout, name='logout'),
    path('config/savePath/', savePath, name='savePath'),
    path('config/newUser/', newUser, name='newUser'),
    path('config/newUser/sendNewUser/', sendNewUser, name='sendNewUser'),
    path('config/scegliPath/', scegliPath, name='scegliPath'),
    path('config/cancellaRunScelta/', cancellaRunScelta, name='cancellaRunScelta'),

    #Dipendenti da backendUtenteScreen
    path('backend/cancellaUtente/<int:ID>/', cancellaUtente, name='cancellaUtente'),

    path('backend/cancellaRun/<int:ID>/', cancellaRun, name='cancellaRun'),

    path('backend/cancellaDirectory/<int:ID>/', cancellaDirectory, name='cancellaDirectory'),

    path('backend/cancellaAgenteDB/<int:ID>/', cancellaAgenteDB, name='cancellaAgenteDB'),
]

