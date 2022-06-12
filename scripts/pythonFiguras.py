# REGISTRO DE VERSIONES
VER = '2022-05-17 bcasas@socib.es'  # Inicio del script
########################################################################################################################


def figuras(inst_type, root, instrumento, instrument_id, file):

    if inst_type == 'URL_TH':
        from pythonFunciones import (plotStation_2Var, leeTempHum, toolCompruebaFolder)
        timeline, var_1, var_2 = leeTempHum(file)
        label_var_1 = 'Temperatura (ºC)'
        label_var_2 = 'Humedad (%)'
        toolCompruebaFolder(root + 'Station/scripts/figuras/')
        output = root + 'Station/scripts/figuras/' + instrument_id + '.png'
        plotStation_2Var(timeline, var_1, var_2, label_var_1, label_var_2, 'r', 'g', instrumento, output)

    if inst_type == 'URL_T':
        from pythonFunciones import (plotStation_1Var, leeTemp, toolCompruebaFolder)
        timeline, var_1 = leeTemp(file)
        label_var_1 = 'Temperatura (ºC)'
        toolCompruebaFolder(root + 'Station/scripts/figuras/')
        output = root + 'Station/scripts/figuras/' + instrument_id + '.png'
        plotStation_1Var(timeline, var_1, label_var_1, 'r', instrumento, output)


# IMPORTA LAS FUNCIONES NECESARIAS
import os
from pythonFunciones import (leeInfo, noInfo, )

########################################################################################################################
# %%

# LOCALIZA EL FICHERO 'info.txt' QUE CONTIENE LA INFORMACION DE LA ESTACION Y DE LOS INSTRUMENETOS INSTALADOS
info = os.path.dirname(os.path.abspath(__file__)) + '/info.txt'
# %%

# COMPRUEBA LA EXISTENCIA DEL FICHERO 'info.txt'
if os.path.isfile(info):
    # SI EXISTE EJECUTA 2 ACCIONES
    ####ACCION_1: REALIZA LA LECTURA DEL FICHERO INFO
    Station, DirLocal, Portal, Puerto, User, DirDest, MailFrom, MailPass, MailDest, Cada, NInstrum, \
    Instrument, Instr_Type, Instr_Id, Param_1, Param_2, Param_3, Param_4, Lines, FileInput = leeInfo(info)

    ####ACCION_2: SE LANZAN LOS PROCESOS DE GRAFICADO DE DATOS PARA CADA INSTRUMENTO
    for n in range(NInstrum):
        figuras(Instr_Type[n], DirLocal, Instrument[n], Instr_Id[n], FileInput[n], )

else:
    # SI NO EXISTE 'info.txt' EJECUTA LA ACCION 3
    ####ACCION_3: NO SE ENCUENTRA EL FICHERO 'info.txt', SE GENERA UN MENSAJE DE ERROR
    noInfo(info)
########################################################################################################################
