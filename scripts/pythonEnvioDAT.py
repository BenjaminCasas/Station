# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 08:27:16 2018
@author: bcasas
"""
# REGISTRO DE VERSIONES
VER = '2022-05-23 bcasas@socib.es'  # Modificaciones para mantener Station
# VER='2021-02-08 benjamin.casas@csic.es' # Modifico la entrada para que coja el banner de las funciones
# VER='2020-08-25 benjamin.casas@csic.es' #Simplifico el script pasando las opciones a pythonFunciones.py
# VER='2019-11-05 benjamin.casas@csic.es' #Anyado la opcion de enviar datos clientraw.txt
# VER='2019-05-12 benjamin.casas@csic.es' #Incluyo el envio de datos de las camaras
# VER='2018-12-19 benjamin.casas@csic.es' #Anyado el tipo rawArchiveFTP
# VER='2018-12-10 benjamin.casas@csic.es' #Corrijo el error de enviar el numero de lineas a la funcion prepara
# VER='2018-12-10 benjamin.casas@csic.es' #Incorporo la lectura del puerto para el SCP del fichero info.txt
# VER='2018-12-10 benjamin.casas@csic.es' #Incorporo el envio a SISMO
# VER='2018-11-09 benjamin.casas@csic.es' #Incorporo el envio de datos clientraw.txt
# VER='2018-10-15 benjamin.casas@csic.es' #Paso las funcions a funciones.py
# VER='2018-10-15 benjamin.casas@csic.es'
# %%

# IMPORTA LAS FUNCIONES NECESARIAS
from pythonFunciones import envioDatos, noInfo, lanzaBanner_SCB
import os
import sys

lanzaBanner_SCB(VER)
# %%

# LOCALIZA LOS FICHEROS 'info.txt' y 'sismo.txt' QUE CONTIENE LA INFORMACION DE LA ESTACION Y DE LOS INSTRUMENETOS
info = os.path.dirname(os.path.abspath(__file__)) + '/info.txt'

# COMPRUEBA SI LLEGA UN ARGUMENTO. SI LLEGA LO GUARDA COMO 'Tipo', SI NO LE ASIGNA 'Tipo=Vacio'
if len(sys.argv) == 1:
    Tipo = 'Vacio'
else:
    Tipo = sys.argv[1]
# %%

# COMPRUEBA LA EXISTENCIA DEL FICHERO 'info.txt'
if os.path.isfile(info):
    # SI EXISTE, SE EJECUTA EL SCRIPT DE ENVIO DE DATOS
    envioDatos(Tipo, info)

else:
    # SI NO EXISTE SEEJECUTA ACCION: NO SE ENCUENTRA EL FICHERO 'info.txt', SE GENERA UN MENSAJE DE ERROR
    noInfo(info)
########################################################################################################################
