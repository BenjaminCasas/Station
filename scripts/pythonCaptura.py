# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 08:27:16 2018
@author: bcasas
"""
#REGISTRO DE VERSIONES
VER='2022-05-15 bcasas@socib.es'         #Modificacion para que la carpeta solo se llame station
#VER='2021-02-17 benjamin.casas@csic.es' #Incluye monitorización de los procesos
#VER='2021-02-08 benjamin.casas@csic.es' #Modifico la entrada para que coja el banner de las funciones
#VER='2020-08-24 benjamin.casas@csic.es' #Modifico captura para que seleccione el tipo automaticamente
#VER='2020-05-21 benjamin.casas@csic.es' #Actualizo versiones
#VER='2020-04-15 benjamin.casas@csic.es' #Incluye SH22
#VER='2019-05-13 benjamin.casas@csic.es' #Incluye las camaras
#VER='2018-12-10 benjamin.casas@csic.es' #Incluye lectura del puerto para scp en info.txt
#VER='2018-10-15 benjamin.casas@csic.es' #Paso las funcions a funciones.py
#VER='2018-10-15 benjamin.casas@csic.es'
########################################################################################################################

#IMPORTA LAS FUNCIONES NECESARIAS
import os
from pythonFunciones import (leeInfo, noInfo, captura, lanzaBanner_SCB)
lanzaBanner_SCB(VER)
########################################################################################################################
#%%

#LOCALIZA EL FICHERO 'info.txt' QUE CONTIENE LA INFORMACION DE LA ESTACION Y DE LOS INSTRUMENETOS INSTALADOS
info = os.path.dirname(os.path.abspath(__file__))+'/info.txt'
#%%

#COMPRUEBA LA EXISTENCIA DEL FICHERO 'info.txt'
if os.path.isfile(info):
#SI EXISTE EJECUTA 2 ACCIONES
####ACCION_1: REALIZA LA LECTURA DEL FICHERO INFO
    Station, DirLocal, Portal, Puerto, User, DirDest, MailFrom, MailPass, MailDest, Cada, NInstrum,\
    Instrument, Instr_Type, Instr_Id, Param_1, Param_2, Param_3, Param_4, Lines, FileInput = leeInfo(info)

####ACCION_2: SE LANZAN LOS PROCESOS DE CAPTURA DE DATOS PARA CADA INSTRUMENTO 
    for n in range (NInstrum):
        captura (Instr_Type[n], DirLocal, Station, Instrument[n], Instr_Id[n],\
                 MailFrom, MailPass, MailDest,\
                 FileInput[n],\
                 Param_1[n] ,Param_2[n] ,Param_3[n] ,Param_4[n], Lines[n] ,)

else:
#SI NO EXISTE 'info.txt' EJECUTA LA ACCION 3
####ACCION_3: NO SE ENCUENTRA EL FICHERO 'info.txt', SE GENERA UN MENSAJE DE ERROR
    noInfo(info)
########################################################################################################################
#%%
