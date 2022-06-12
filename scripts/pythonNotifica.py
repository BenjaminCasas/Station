#REGISTRO DE VERSIONES
VER='2022-06-02 bcasas@socib.es'         #Creo este script a partir del que hay en apcupsd

#IMPORTA LAS FUNCIONES NECESARIAS
import os
import sys
from pythonFunciones import toolAnyadeLog, leeInfo, toolInstant

#LOCALIZA EL FICHERO 'info.txt' QUE CONTIENE LA INFORMACION DE LA ESTACION Y DE LOS INSTRUMENETOS INSTALADOS
info = os.path.dirname(os.path.abspath(__file__))+'/info.txt'

# LEE EL ARGUMENTO, QUE CONTIENE EL MENSAJE A ENVIAR
TEXT = toolInstant('%Y-%m-%d %H:%M:%S')+' | LOG_'+sys.argv[1]+'. '+sys.argv[2]
#%%

# ACCION_1: REALIZA LA LECTURA DEL FICHERO INFO
Station,DirLocal,Portal,Puerto,User,DirDest,MailFrom,MailPass,MailDest,Cada,NInstrum,Instrument,Instr_Type,Instr_Id,Param_1,Param_2,Param_3,Param_4,Lines,FileInput = leeInfo(info)
#%%

# ACCION_2: ESCRIBE EN EL FICHERO LOG Y ENVIA EL CORREO
toolAnyadeLog(DirLocal, Station,sys.argv[1],TEXT, MailFrom, MailPass, MailDest)
#%%