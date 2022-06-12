# -*- coding: utf-8 -*-
"""
Created on Thu Nov 08 11:35:16 2018
@author: bcasas
"""
VER = '2022-06-03 bcasas@socib.es'  # Elimino la función capturaDHT22_sht1X. Actualizo capturaDHT22_adafruit


# VER = '2022-05-26 bcasas@socib.es'        # Corrijo un error en leeInfo
# VER = '2022-05-15 bcasas@socib.es'        #Modifico: NoInfo, toolAnyadeLog
# VER = '2021-07-16 benjamin.casas@csic.es' #Añado funciones para pintar datos de Vector
# VER = '2021-06-06 benjamin.casas@csic.es' #Añado funciones para pintar datos de Aquadopp
# VER = '2021-05-22 benjamin.casas@csic.es' #Añado funciones para monitoreo de las estaciones
# VER = '2021-02-17 benjamin.casas@csic.es' #Pongo orden en las funciones e incluyo la monitorización de los procesos
# VER = '2021-02-08 benjamin.casas@csic.es' #Modifico el try: except en capturaSerie para mejorar su funcionamiento
# VER = '2021-01-14 benjamin.casas@csic.es' #Añado la posibilidad de incorporar datos de una base de datos creada por la
#                                           #aplicacion Weewx
# VER = '2021-01-02 benjamin.casas@gmail.com' #Añado una función para capturar datos desde un entorno web montado en
#                                           #un ESP8266
# VER = '2020-10-13 benjamin.casas@csic.es' #Modifico el script de captura DS18B20 para registrar de diferentes sensores
#                                           #conectados en serie
# VER = '2020-09-09 benjamin.casas@csic.es' #Modifico el script de captura de datos AADI para que almacene sienpre
#                                           #los datos raw
# VER = '2020-09-07 benjamin.casas@csic.es' #Modifico los scripts de captura de datos que realizan una consulta para
#                                           #que lo hagan de forma programada con "programador"
# VER = '2020-07-27 benjamin.casas@csic.es' #Añado envio de datos por diversos metodos. Alado la funcion getSize
# VER = '2020-07-23 benjamin.casas@csic.es' #Añado una función para leer datros del sensor DS18B20
# VER = '2020-05-21 benjamin.casas@csic.es' #Añado las funciones de captura de datos del sensor DHT22 (adafruit y shx1)
# VER = '2020-05-06 benjamin.casas@csic.es' # odifico la funcion de borrado de camaras para borrar fichero con python
# VER = '2020-04-29 nwirth@socib.es'        #Añadido la funcion BORRADO DE CAMARAS, se borran los imagenes de las
#                                           #CAMARAS despues ()dias
# VER = '2020-04-06 benjamin.casas@csic.es' #Añado el hostname y la dirección ip-wan en el envio de los avisos por
#                                           #correo electrionico
# VER = '2019-10-24 benjamin.casas@csic.es' #Modifico el envio de datos de las CAMARAS
# VER = '2019-11-05 benjamin.casas@csic.es' #Empieza la creacion del fichero clientraw.txt
# VER = '2019-10-05 benjamin.casas@csic.es' #Modifico captura para eliminar las lineas en blanco
#                                           #(problema en la meteo de Galfi)
# VER = '2019-05-29 benjamin.casas@csic.es' #Modifico captura para leer datos del sensor de temperatura
# VER = '2018-12-17 benjamin.casas@csic.es' #Modifico la funcion 'envio' para que cuando el tipo sea rawArchiveFTP
#                                           #copie el contenido de la carpeta rawArchiveFTP a rawArchive en lugar de
#                                           #borrarla
# VER = '2018-12-13 benjamin.casas@csic.es' #funcion 'pepara'. Añado una condicion para que los ficheros SISMO no
#                                           #revisen el ultimo dato registrado
# VER = '2018-12-13 benjamin.casas@csic.es' #Corrijo el envio de numero de lineas en el tail de la funcion prepara
########################################################################################################################
#
#
#
# LISTA DE FUNCIONES DISPONIBLES:
#  1-leeInfo                | Lee el fichero de informacion donde estan los datos que se utilizaran en el proceso
#  2-leeInfoIns             |
#  3-leeInfoBuoy            | Lee la información que necesita pythonWatchPi.py para chequear el estado de las boyas
#  4-leeDataCAMPBELL_status | Lee los datos registrados por el DL CAMPBELL en boyas. Se utiliza en pythonWatchPi.py
#  5-leeDataAXYX_status     | Lee los datos registrados por el DL AXYS en boyas. Se utiliza en pythonWatchPi.py
#
#  8-leeCalAADI             | Lee los datos de calibracion de los instrumentos Aanderaa
#  9-noInfo                 | Genera un mensaje informando de que no encuentra el fichero info.txt
# ...
# 11-captura                | Inicia la captura de datos
# 12-captura_SERIE          | Captura de datos por puerto serie
# 13-captura_AADI           | Captura de datos de instrumentos Aanderaa
# 14-captura_DTH22_adafruit | Captura datos recogidos por un sensor DTH22 con libreria Adafruit
# 15-captura_DTH22_sht1x    | Captura datos recogidos por un sensor DTH22 con libreria SHT1X
# 16-captura_DS18B20        | Captura datos recogidos por un sensor DS18B20
# 17-captura_PiCAM          | Captura datos con la PiCAM
# 18-captura_URL-TH         | Captura dataos de Temperatura y humedad de una URL
# 19-captura_URL_T          | Captura dataos de Temperatura de una URL
# 20-captura_DAVIS_Weewx    | Captrura datos de una base de datos creada por el software Weewx
# ...
# 31-envioDatos             | Envio de datos en funcion del TIPO
# 32-envioPrepara           | Prepara datos para ser enviados al servidor
# 33-envioPreparaDia        | Prepara los ficheros diarios para er enviados al servidor
# 34-envioPreparaCAM        | Prepara imagenes tomadas por las WebCam para ser enviadas al servidor
# 35-envioEnvia             | Envia datos al servidor
# 26-envioBorra             | Borra los archivos enviados
# 37-envioBorraCAM          | Borra imagenes de las camaras mas antiguas de un numero de dias determinado
# ...
# 41-monitor
# 42-compruebaSubprocesos
# 43-compruebaRecepcion
# 44-compruebaPosiocion
# 45-compruebaVoltaje
# 46-compruebaTemperatura
# 47-compruebaAnteriorProblema
# 47-compruebaUltimo
# ...
# 61-toolInstant            | Calcula el instante temporal
# 62-toolHaversie:          | Funcióm para calcular la distancia entre dos puntos
# 63-toolGetSize            | Funcion para calcular el espacio ocupado en un directorio
# 64-toolSendMail           | Notifica por correo electronico
# 65-toolAnyadeLog          | Anyade informacion a los logs
# 66-toolmantenerTamanyoLog | Mantiene el tamaño de los logs en 5000 líneas como máximo
# 67-toolEncuentraFichero
# 68-toolEncuentraFicherosDaily  | Busca todos los ficheros que hay en la carpeta rawArchiverDaily.
#                                  Utilizado en pythonWatchPi.py para hacer las figuras
# 69-toolEncuentraEncuentraEXT   | Busca todos los ficheros con una determinada extensión que hay dentro
#                              de un directorio
# ...
# 81-programador            | Funcion que programa la toma de datos
# 82-prog_Calcula_INI       | Funcion que calcula el inicio de la programación de las tareas
# 83-prog_TareaLanza        | Funcion que lanza la ejecucion de las tareas
# 84-prog_TareaEjecuta      | Funcion que ejecuta las tareas
# ...
# 91-lanzaBanner_IME
# 92-lanzaBanner_SBE
# ...
# 101-plot_2X2Serie
# 102-plot_posicion
########################################################################################################################
########################################################################################################################
#
#
#
# LECTURA DE FICHEROS INFO.txt
########################################################################################################################

# 1-leeInfo: LEE LA INFORMACION DEL FICHERO 'info.txt'#########################
def leeInfo(info):
    import time
    FileName = time.strftime('%Y%m%d') + '.ail'

    print('-funcionesVersion: ' + VER + '-')
    print(' ')
    print(' ')

    Instrument = []
    Instr_Type = []
    Instr_Id = []
    Param_1 = []
    Param_2 = []
    Param_3 = []
    Param_4 = []
    Lines = []
    FileInput = []

    f_info = open(info, 'r')
    datos = f_info.readlines()
    Station = datos[0].split('"')[1]
    DirLocal = datos[1].split('"')[1]
    Portal = datos[2].split('"')[1]
    Puerto = datos[3].split('"')[1]
    User = datos[4].split('"')[1]
    DirDest = datos[5].split('"')[1]
    MailFrom = datos[6].split('"')[1]
    MailPass = datos[7].split('"')[1]
    MailDest = datos[8].split('"')[1]
    Monitor = datos[9].split('"')[1]
    NInstrum = int(datos[11].split('"')[1])

    for n in range(NInstrum):
        Instrument.append(datos[(13 + 10 * n)].split('"')[1])
        Instr_Type.append(datos[(14 + 10 * n)].split('"')[1])
        Instr_Id.append(datos[(15 + 10 * n)].split('"')[1])
        Param_1.append(datos[(16 + 10 * n)].split('"')[1])
        Param_2.append(datos[(17 + 10 * n)].split('"')[1])
        Param_3.append(datos[(18 + 10 * n)].split('"')[1])
        Param_4.append(datos[(19 + 10 * n)].split('"')[1])
        Lines.append(datos[(20 + 10 * n)].split('"')[1])
        FileInput.append(DirLocal + 'Station/' + Instrument[n] + '/rawInput/' + FileName)
        # FileInput.append(DirLocal + 'Station/' + Instrument[n] + '/rawInput/rawData-' + datos[(14+9*n)].split('"')[1] +'.ail')
    f_info.close()
    del datos, n
    return Station, DirLocal, Portal, Puerto, User, DirDest, MailFrom, MailPass, MailDest, Monitor, NInstrum, Instrument, Instr_Type, Instr_Id, Param_1, Param_2, Param_3, Param_4, Lines, FileInput


########################################################################################################################
#
#
# 2-leeInfoIns: LEE LA INFORMACION DE LA COMPOSICION DE CADA ESTACION##########
def leeInfoInst(info):
    Inst_name = []
    Inst_cada = []

    f_info = open(info, 'r')
    datos = f_info.readlines()
    MailDest = datos[1].split('"')[1]
    N_Inst = int(datos[2].split('"')[1])

    for n in range(N_Inst):
        Inst_name.append(datos[(5 + 3 * n)].split('"')[1])
        Inst_cada.append(datos[(6 + 3 * n)].split('"')[1])

    f_info.close()

    del datos, n
    return N_Inst, Inst_name, Inst_cada, MailDest


########################################################################################################################
#
#
# 3-leeInfoBuoy: LEE LA INFORMACION DEL PARA CHEQUEAR LOS DATOS DE LAS BOYAS. EMPEADO EN pythonWatchPi.py###############
def leeInfoBuoy(info):
    #    import time

    print('-funcionesVersion: ' + VER + '-')
    print(' ')
    print(' ')

    #    FileName = time.strftime('%Y%m%d')+'.ail'
    estName = []
    estConx = []
    estRemo = []
    estData = []
    estTipo = []
    LAT_REF = []
    LON_REF = []
    RADI_UMB = []
    BVOL_UMB = []
    ITEM_UMB = []
    CADA = []

    f_info = open(info, 'r')
    datos = f_info.readlines()
    DirLocal = datos[1].split('"')[1]
    MntPoint = datos[2].split('"')[1]
    WebSrv = datos[3].split('"')[1]
    MailFrom = datos[4].split('"')[1]
    MailPass = datos[5].split('"')[1]
    MailDest = datos[6].split('"')[1]
    NEstacio = int(datos[7].split('"')[1])

    for n in range(NEstacio):
        estName.append(datos[(10 + 13 * n)].split('"')[1])
        estConx.append(datos[(11 + 13 * n)].split('"')[1])
        estRemo.append(datos[(12 + 13 * n)].split('"')[1])
        estData.append(datos[(13 + 13 * n)].split('"')[1])
        estTipo.append(datos[(14 + 13 * n)].split('"')[1])
        LAT_REF.append(datos[(15 + 13 * n)].split('"')[1])
        LON_REF.append(datos[(16 + 13 * n)].split('"')[1])
        RADI_UMB.append(datos[(17 + 13 * n)].split('"')[1])
        BVOL_UMB.append(datos[(18 + 13 * n)].split('"')[1])
        ITEM_UMB.append(datos[(19 + 13 * n)].split('"')[1])
        CADA.append(datos[(20 + 13 * n)].split('"')[1])
    f_info.close()
    del datos, n
    return DirLocal, MntPoint, WebSrv, MailFrom, MailPass, MailDest, estName, estConx, estRemo, estData, estTipo, LAT_REF, LON_REF, RADI_UMB, BVOL_UMB, ITEM_UMB, CADA


########################################################################################################################
#
#
# 4-leeDataCAMPBELL_status: LEE LOS DATOS REGISTRADOS POR EL DL CAMPBELL DE LAS BOYAS
def leeDataCAMPBELL_status(DIR, FICHEROS, Lat_REF, Lon_REF):
    import csv
    from datetime import datetime

    DATE = []
    LATI = []
    LONG = []
    DIST = []
    NSAT = []
    PITC = []
    ROLL = []
    ITEM = []
    BVOL = []
    for N in range(len(FICHEROS)):
        FICHERO = DIR + '/' + FICHEROS[N]
        # print (FICHERO)
        with open(FICHERO, newline='') as csvfile:
            info = csv.reader(csvfile, delimiter=',')
            for ROW in info:
                if (ROW[0][0:2] == '20'):
                    DATE.append(datetime.strptime(ROW[0], '%Y-%m-%d %H:%M:%S'))
                    LAT = (ROW[6])
                    LAT = float(LAT[0:2]) + (float(LAT[2:]) / 60)
                    LATI.append(LAT)
                    LON = (ROW[7])
                    LON = float(LON[0:3]) + (float(LON[3:]) / 60)
                    LONG.append(LON)
                    DIST.append(round(toolHaversine(float(Lat_REF), float(Lon_REF), float(LAT), float(LON)), 1))
                    NSAT.append(float(ROW[8]))
                    PITC.append(float(ROW[9]))
                    ROLL.append(float(ROW[10]))
                    ITEM.append(float(ROW[12]))
                    BVOL.append(float(ROW[13]))

    return DATE, LATI, LONG, DIST, ITEM, BVOL


########################################################################################################################
#
#
# 5-leeDataAXYS_status: LEE LOS DATOS REGISTRADOS POR EL DL AXYS DE LAS BOYAS
def leeDataAXYS_status(DIR, FICHEROS, Lat_REF, Lon_REF):
    import csv
    from datetime import datetime

    DATE = []
    LATI = []
    LONG = []
    DIST = []
    # NSAT = []
    # PITC = []
    # ROLL = []
    ITEM = []
    BVOL = []
    for N in range(len(FICHEROS)):
        FICHERO = DIR + '/' + FICHEROS[N]
        # print (FICHERO)
        with open(FICHERO, newline='') as csvfile:
            info = csv.reader(csvfile, delimiter=',')
            for ROW in info:
                if (ROW[5] == '1'):
                    DATE.append(datetime(int('20' + ROW[2][0:2]), int(ROW[2][2:4]), int(ROW[2][4:6]), int(ROW[3][0:2]),
                                         int(ROW[3][2:4]), int(ROW[3][4:6])))
                    LAT = (ROW[8])
                    LAT = float(LAT[0:2]) + (float(LAT[2:9]) / 60)
                    LATI.append(LAT)
                    LON = (ROW[9])
                    LON = float(LON[0:1]) + (float(LON[1:8]) / 60)
                    LONG.append(LON)
                    DIST.append(round(toolHaversine(float(Lat_REF), float(Lon_REF), float(LAT), float(LON)), 1))
                    # NSAT.append (float(ROW[8]))
                    # PITC.append (float(ROW[9]))
                    # ROLL.append (float(ROW[10]))
                    ITEM.append(float(ROW[14]))
                    BVOL.append(float(ROW[7]))

    return DATE, LATI, LONG, DIST, ITEM, BVOL


########################################################################################################################
#
#
# 8-leeCalAADI: FUNCION DE LECTURA DE CALIBRACION AADI#########################
def leeCalAADI(FileName):
    # print 'Fichero de calibraciones:'+FileName
    CAL_MTX = []
    FILE = open(FileName, 'r')
    LINE = FILE.readlines()
    CONT = 0
    for LINE in open(FileName, 'r'):
        lista = (LINE.split(",")[0], LINE.split(",")[1], LINE.split(",")[2], LINE.split(",")[3], LINE.split(",")[4])
        CAL_MTX.append(lista)
        CONT = CONT + 1
    FILE.close()
    return CAL_MTX


###############################################################################
#
#
# 9-noInfo: FUNCION PARA FRECUENTE DE DATOS####################################
def noInfo(info):
    import os
    text = 'ERROR: No se encuentra el fichero de informacion de la estacion:' + info
    print(text)
    text = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_CAPTURA. ' + text
    root, lev_1, lev_2 = toolSepara2LevelNF(os.path.dirname(os.path.abspath(__file__)))

    print('path =' + os.path.dirname(os.path.abspath(__file__)))
    print('Root =' + root)
    print('lev_1=' + lev_1)
    print('lev_2=' + lev_2)

    toolAnyadeLog(root, 'NoStation', 'ERROR', text, '-', '-', '-')
    print('    -EL SCRIPT SE HA DETENIDO-')


########################################################################################################################
#
#
#
# CAPTURA DE DATOS
########################################################################################################################
########################################################################################################################
#
# 11-captura: FUNCION PARA CAPTURA DE DATOS#####################################
def captura(TIPO, ROOT, STATION, INSTRUMENT, INSTRUMENT_ID, MailFROM, MailPASS, MailDEST, FileINPUT, PARAM_1, PARAM_2,
            PARAM_3, PARAM_4, LINEAS):
    from threading import Thread
    if (
            TIPO == 'DS18B20' or TIPO == 'DTH22_adafruit' or TIPO == 'DTH22_sht1x' or TIPO == 'PiCAM' or TIPO == 'DAVIS_Weewx'):
        TEXT = 'Se va a ejecutar la captura de datos del sensor ' + INSTRUMENT + ' tomando datos cada ' + str(
            PARAM_1) + 's'
        print(TEXT)
        TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_CAPTURA. ' + TEXT
        toolAnyadeLog(ROOT, STATION, 'LOG', TEXT, '-', '-', '-')
        if (TIPO == 'PiCAM'):
            TXT = PARAM_2
            if (PARAM_2 == 'FOTO'): TXT = 'Las imagenes tomadas por '
            if (PARAM_2 == 'TIMELAPSE'): TXT = 'Las imagenes del TIMELAPSE tomadas por '
            if (PARAM_2 == 'VIDEO'): TXT = 'Los videos tomados por '
            TEXT = TXT + INSTRUMENT + ' se almacenaran en: ' + FileINPUT[0:FileINPUT.rfind('/')]

        else:
            TEXT = 'Los datos de ' + INSTRUMENT + ' se almacenaran en: ' + FileINPUT
        print(TEXT)
        print('  ')
        TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_CAPTURA. ' + TEXT
        toolAnyadeLog(ROOT, STATION, 'LOG', TEXT, '-', '-', '-')
        FUNCION = 'captura_' + TIPO
        subproceso = Thread(target=programador, args=(
            FUNCION, FileINPUT, PARAM_1, PARAM_2, PARAM_3, PARAM_4, ROOT, STATION, MailFROM, MailPASS, MailDEST))
        subproceso.start()

    elif (TIPO == 'URL_TH' or TIPO == 'URL_T'):
        print()
        TEXT = 'Se va a ejecutar la captura de datos de la URL ' + str(
            PARAM_2) + ' que contiene datos del sensor ' + INSTRUMENT + ' cada ' + str(PARAM_1) + 's'
        print(TEXT)
        TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_CAPTURA. ' + TEXT
        toolAnyadeLog(ROOT, STATION, 'LOG', TEXT, '-', '-', '-')
        TEXT = 'Los datos de ' + INSTRUMENT + ' se almacenaran en: ' + FileINPUT
        print(TEXT)
        FUNCION = 'captura_' + TIPO
        subproceso = Thread(target=programador, args=(
            FUNCION, FileINPUT, PARAM_1, PARAM_2, PARAM_3, PARAM_4, ROOT, STATION, MailFROM, MailPASS, MailDEST))
        subproceso.start()

    elif (TIPO == 'CAM'):
        print('Ejecuto el proceso de borrado de imagenes de la camara')
        envioBorraCAM(ROOT, STATION, INSTRUMENT, LINEAS)

    elif (TIPO == 'SERIE'):
        # print ('Ejecuto el proceso de captura de datos por puerto serie')
        subproceso = Thread(name='thr' + INSTRUMENT, target=captura_SERIE, args=(
            FileINPUT, PARAM_1, int(PARAM_2), int(PARAM_3), PARAM_4, ROOT, STATION, INSTRUMENT, MailFROM, MailPASS,
            MailDEST,))
        subproceso.start()

    elif (TIPO == 'AADI'):
        # print ('Ejecuto el proceso de captura de datos AADI')
        subproceso = Thread(target=captura_AADI, args=(
            FileINPUT, PARAM_1, int(PARAM_2), int(PARAM_3), PARAM_4, ROOT, STATION, INSTRUMENT, INSTRUMENT_ID, MailFROM,
            MailPASS, MailDEST,))
        subproceso.start()

    else:
        TEXT = 'ERROR_Inicio. Tipo de instrumento no definido. No se realiza ninguna accion con este instrumento --- Instr_TYPE=' + TIPO + ' ---'
        print(TEXT)
        TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ' + TEXT
        toolAnyadeLog(ROOT, STATION, 'ERROR', TEXT, MailFROM, MailPASS, MailDEST)


########################################################################################################################
#
#
# 12-captura_SERIE: FUNCION PARA CAPTURA DE DATOS POT PUERTO SERIE #############
def captura_SERIE(File, Port, Baud, BitSize, Parity, Root, Station, Instrument, MailFrom, MailPass, MailDest):
    import serial
    import time
    toolPreparaDir(File)
    SerialCapture = serial.Serial(Port, baudrate=Baud, bytesize=BitSize, parity=Parity)
    flag = 1
    TEXT = 'Se va a ejecutar la captura de datos para el puerto ' + Port + ' ' + str(Baud) + '-' + str(
        BitSize) + '-' + Parity
    print(TEXT)
    TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_CAPTURA. ' + TEXT
    toolAnyadeLog(Root, Station, 'LOG', TEXT, 'from', 'pass', 'to')
    TEXT = 'Los datos de ' + Instrument + ' se almacenaran en: ' + File
    print(TEXT)
    print('  ')
    TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_CAPTURA. ' + TEXT
    toolAnyadeLog(Root, Station, 'LOG', TEXT, 'from', 'pass', 'to')
    while (flag):
        # print('Instrument= '+str(Instrument.find('TEMP')))
        if (Instrument.find('TEMP') > 0):
            InputSerial = SerialCapture.read(size=11)
        else:
            InputSerial = SerialCapture.readline()
            InputSerial = InputSerial.strip()

        try:
            InputSerial = InputSerial.decode("utf-8", "ignore")
            InputDate = time.strftime("%Y-%m-%d %H:%M:%S")
            DataLine = InputDate + ' | ' + InputSerial + '\n'
            # print (DataLine)
            FileInput = open(File, 'a')
            FileInput.write('%s' % DataLine)
            FileInput.close()
        except(IOError, NameError) as ERROR:
            TEXT = 'Se ha producido un error en la adquisición de datos del instrumento ' + Instrument + ' ERROR:' + str(
                ERROR)
            print(TEXT)
            TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + TEXT

            toolAnyadeLog(Root, Station, 'ERROR', TEXT, MailFrom, MailPass, MailDest)


########################################################################################################################
#
#
# 13-captura_AADI: FUNCION DE CAPTURA DE DATOS AADI#############################
def captura_AADI(File, Port, Baud, BitSize, Parity, Root, Station, Instrument, Instrument_ID, MailFrom, MailPass,
                 MailDest):
    import serial
    import os
    toolPreparaDir(File)
    ROOT, FOLDER_1, FOLDER_2, FILE = toolSepara2Level(File)
    toolPreparaDir(ROOT + FOLDER_1 + '/rawArchive/')

    FileRaw = File.find('.')
    FileRaw = File[:FileRaw] + '.raw'
    I = FileRaw.find('raw')
    FileRaw = FileRaw[:I] + 'rawArchive' + FileRaw[I + 8:]
    FileCal = Root + Station + '/scripts/calibraciones/' + Instrument_ID + '.cal'

    TEXT = 'Se va a ejecutar la captura de datos para el puerto ' + Port + ' ' + str(Baud) + '-' + str(
        BitSize) + '-' + Parity
    print(TEXT)
    TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_CAPTURA. ' + TEXT
    toolAnyadeLog(Root, Station, 'LOG', TEXT, 'from', 'pass', 'to')
    TEXT = 'Los datos convertidos (.ail) de ' + Instrument + ' van a: ' + File
    print(TEXT)
    TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_CAPTURA. ' + TEXT
    toolAnyadeLog(Root, Station, 'LOG', TEXT, 'from', 'pass', 'to')
    TEXT = 'Los datos originales  (.raw) de ' + Instrument + ' van a: ' + FileRaw
    print(TEXT)
    TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_CAPTURA. ' + TEXT
    toolAnyadeLog(Root, Station, 'LOG', TEXT, 'from', 'pass', 'to')
    print('  ')

    ##Busca el fichero de calibracion y lo carga
    if os.path.isfile(FileCal):
        cal_mtx = leeCalAADI(FileCal)
        REF = cal_mtx[0][0]
    else:
        print('ERROR, no se encuentra el fichero de calibracion')
        TEXT = toolInstant(
            '%Y-%m-%d %H:%M:%S') + ' | ERROR_captura_AADI. No se ha encontrado el fichero de calibracion: ' + FileCal
        toolAnyadeLog(Root, Station, 'ERROR', TEXT, MailFrom, MailPass, MailDest)

    ##Realiza la captura de datos por el puerto serie
    SerialCapture = serial.Serial(Port, baudrate=Baud, bytesize=BitSize, parity=Parity)
    flag = 1
    while (flag):
        ##Captura los datos del puerto serie
        InputSerial = SerialCapture.readline()
        InputSerial = InputSerial.decode("utf-8")
        InputDate = toolInstant("%Y-%m-%d %H:%M:%S")
        # print ('      InputSerial= '+InputSerial)

        ##Guarda los datos raw
        DAT = []
        DAT.append(InputSerial[0:len(InputSerial)])
        DAT = str(DAT)
        # print ('DAT='+DAT)
        POS = DAT.find('r')
        # print ('POS='+str(POS))
        if (POS == -1):
            DataLineRAW = InputDate + ' | ' + InputSerial
        else:
            DataLineRAW = InputDate + ' | ' + DAT[POS + 1:len(InputSerial) + 2] + '\n'

        # print ('DataLine= '+DataLineRAW)
        FileIRaw = open(FileRaw, 'a')
        FileIRaw.write('%s' % DataLineRAW)
        FileIRaw.close()

        ##Guarda los datos calibrados
        if (REF != ''):
            INI = InputSerial.find(REF)
            if INI == -1:
                TEXT = 'ERROR_captura_AADI. En la linea de datos de entrada no se ha encontrado la referencia esperada: ' + REF + ' Se encontro en su lugar: ' + InputSerial[
                                                                                                                                                                 0:5]
                print(TEXT)
                TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ' + TEXT
                toolAnyadeLog(Root, Station, 'ERROR', TEXT, MailFrom, MailPass, MailDest)
            else:
                FileInput = open(File, 'a')
                DataENG = []
                for NVAR in range(len(cal_mtx) - 1):
                    RAW = int(InputSerial[INI + NVAR * 5:NVAR * 5 + (INI + 4)])
                    ENG = float(cal_mtx[NVAR + 1][1]) + float(cal_mtx[NVAR + 1][2]) * RAW + float(
                        cal_mtx[NVAR + 1][3]) * RAW * RAW + float(cal_mtx[NVAR + 1][4]) * RAW * RAW * RAW
                    # print 'RAW '+str(cal_mtx[NVAR+1][0])+'= '+str(RAW)
                    # print 'ENG '+str(cal_mtx[NVAR+1][0])+'= '+str(ENG)
                    DataENG.append(ENG)
                DataLineENG = InputDate + ' | ' + '0R0,Dm=' + str(int(DataENG[3])) + 'D,Dx=-D,Sm=' + str(
                    round(DataENG[1], 1)) + 'M,Sx=' + str(round(DataENG[2], 1)) + 'M,Ta=' + str(
                    round(DataENG[4], 2)) + 'C,Ua=' + str(round(DataENG[5], 1)) + 'P,Pa=' + str(
                    round(DataENG[6], 1)) + 'H,Rc=-M,Rd=-s,Ri=-M,Rp=-M,Vs=-,NRad=' + str(
                    round(DataENG[7], 1)) + 'W/sqm' + '\n'
                # print 'Datos RAW= '+DataLineRAW
                # print 'Datos ENG= '+DataLineENG
                # print '-'
                FileInput.write('%s' % DataLineENG)
                FileInput.close()


########################################################################################################################
#
#
# 14-captura_DTH22_adafruit: FUNCION DE CAPTURA DE DATOS DTH22##################
def captura_DTH22_adafruit(file, DataPin, GroundPin, VoltPin, ROOT, STATION, MailFROM, MailPASS, MailDEST):
    import adafruit_dht as dht
    import board
    from time import strftime
    toolPreparaDir(file)


    dhtDevice = dht.DHT22(board.D+ str(DataPin), use_pulseio=False)
    try:
        temp = dhtDevice.temperature
        hum = dhtDevice.humidity
    except:
        temp = 'NaN'
        hum = 'NaN'

    InputDate = strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(hum, float) and isinstance(temp, float):
        if hum > 100 or temp < 15:
            InputData = 'Temp=NaN   Hum=NaN'
        else:
            InputData = ('Temp={0:0.1f}C Hum={1:0.1f}%'.format(temp, hum))
    else:
        InputData = 'Temp=NaN   Hum=NaN'
    DataLine = InputDate + ' | ' + InputData + '\n'
    # print (DataLine)
    FileInput = open(File, 'a')
    FileInput.write('%s' % DataLine)
    FileInput.close()


########################################################################################################################
#
#
# 16-captura_DS18B20: FUNCION DE CAPTURA DE DATOS DS18B20#######################
def captura_DS18B20(File, DataPin, GroundPin, Sensor_N, ROOT, STATION, MailFROM, MailPASS, MailDEST):
    # Es necesario activar en la RPi el interfaz de comunicacion 1-Wire
    import os
    import glob
    from time import strftime
    toolPreparaDir(File)
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[int(Sensor_N)]
    device_file = device_folder + '/w1_slave'

    # print ('device_file= '+device_file)

    def lee_DS18B20_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    lines = lee_DS18B20_raw()
    if lines[0].strip()[-5:] != 'YES':
        # time.sleep(0.2)
        lines = lee_DS18B20_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            TEM_str = lines[1][equals_pos + 2:]
            try:
                TEM = float(TEM_str) / 1000.0
                InputData = ('Temp={0:0.1f}C'.format(TEM))
            except ValueError:
                InputData = ('Temp=NaN')
            InputDate = strftime("%Y-%m-%d %H:%M:%S")
            DataLine = InputDate + ' | ' + InputData + '\n'
            # print (DataLine)
            FileInput = open(File, 'a')
            FileInput.write('%s' % DataLine)
            FileInput.close()


########################################################################################################################
#
#
# 17-captura_PiCAM: FUNCION DE CAPTURA DE DATOS CON LA PiCAM####################
def captura_PiCAM(DIR, MODO, PARAM_3, PARAM_4, ROOT, STATION, MailFROM, MailPASS, MailDEST):
    # Es necesario activar en la RPi el interfaz de comunicacion 1-Wire
    import os
    DIR = DIR[0:DIR.rfind('/')]
    if (MODO == 'FOTO'):
        FILE = DIR + '/FOTO_' + toolInstant('%Y%m%d_%H%M%S') + '.jpg'
        # print (toolInstant('%Y%m%d_%H%M%S')+' - Tomando la imagen '+FILE)
        COMMAND = 'raspistill -q ' + str(PARAM_3) + ' ' + str(PARAM_4) + ' -o ' + FILE
    elif (MODO == 'TIMELAPSE'):
        FILE = DIR + '/TIMELAPSE_' + toolInstant('%Y%m%d_%H%M%S') + '_%03d.jpg'
        COMMAND = 'raspistill -t ' + str(PARAM_3) + ' -tl ' + PARAM_4 + ' -o ' + FILE
    elif (MODO == 'VIDEO'):
        print('PENDIENTE')
        FILE = DIR + '/VIDEO_' + toolInstant('%Y%m%d_%H%M%S') + '.h264'
        COMMAND = 'raspivid -t ' + str(PARAM_3) + ' ' + str(PARAM_4) + ' -o ' + FILE
    else:
        print('NO RECONOZCO ESTE MODO: ' + MODO)
        COMMAND = 'ls'

    os.system(COMMAND)


########################################################################################################################
#
#
# 18-captura_URL_TH: FUNCION PARA CAPTURA DE DATOS DE UNA PAGINA WEB ######
def captura_URL_TH(File, URL, Param_3, Param_4, ROOT, STATION, MailFROM, MailPASS, MailDEST):
    import urllib.request
    from time import strftime
    from bs4 import BeautifulSoup

    toolPreparaDir(File)

    try:
        urllib.request.urlopen(URL, timeout=10)
        WEB = urllib.request.urlopen(URL).read().decode()
        SOUP = BeautifulSoup(WEB, 'html.parser')
        DATALINE = strftime("%Y-%m-%d %H:%M:%S | ")
        COUNT = 1
        for OUTPUT in SOUP.find_all('span'):
            if (COUNT == 2):
                TEMP = OUTPUT.text
            elif (COUNT == 4):
                HUM = OUTPUT.text
            COUNT = COUNT + 1
        try:
            TEMP = float(TEMP)
            HUM = float(HUM)
            DATALINE = DATALINE + ('Temp={0:0.1f}C Hum={1:0.1f}%'.format(TEMP, HUM)) + '\n'
        except ValueError:
            DATALINE = strftime("%Y-%m-%d %H:%M:%S | Temp=NaNC Hum=NaN%" + '\n')

        # print (DATALINE)
        FileInput = open(File, 'a')
        FileInput.write('%s' % DATALINE)
        FileInput.close()
    except urllib.error.URLError as e:
        TEXT = 'Error_Captura. La URL ' + URL + ' No está disponible' + ' | ' + str(e.reason)
        TEXT = strftime("%Y-%m-%d %H:%M:%S | ") + TEXT
        print('\n' + TEXT + '\n')
        toolAnyadeLog(ROOT, STATION, 'ERROR', TEXT, MailFROM, MailPASS, MailDEST)


########################################################################################################################
#
#
# 19-captura_URL_T: FUNCION PARA CAPTURA DE DATOS DE UNA PAGINA WEB ######
def captura_URL_T(File, URL, Param_3, Param_4, ROOT, STATION, MailFROM, MailPASS, MailDEST):
    import urllib.request
    from time import strftime
    from bs4 import BeautifulSoup
    toolPreparaDir(File)
    try:
        urllib.request.urlopen(URL, timeout=10)
        WEB = urllib.request.urlopen(URL).read().decode()
        SOUP = BeautifulSoup(WEB, 'html.parser')
        DATALINE = strftime("%Y-%m-%d %H:%M:%S | ")
        COUNT = 1
        for OUTPUT in SOUP.find_all('span'):
            if (COUNT == 2):
                TEMP = OUTPUT.text
            COUNT = COUNT + 1
        try:
            TEMP = float(TEMP)
            DATALINE = DATALINE + ('Temp={0:0.2f}C '.format(TEMP)) + '\n'
        except ValueError:
            DATALINE = strftime("%Y-%m-%d %H:%M:%S | Temp=NaNC %" + '\n')

        # print (DATALINE)
        FileInput = open(File, 'a')
        FileInput.write('%s' % DATALINE)
        FileInput.close()
    except urllib.error.URLError as e:
        TEXT = 'Error_Captura. La URL ' + URL + ' No está disponible' + ' | ' + str(e.reason)
        TEXT = strftime("%Y-%m-%d %H:%M:%S | ") + TEXT
        print('\n' + TEXT + '\n')
        toolAnyadeLog(ROOT, STATION, 'ERROR', TEXT, MailFROM, MailPASS, MailDEST)


########################################################################################################################
#
#
# 20-captura_DAVIS_Weewx: FUNCION PARA CAPTURA DE DATOS DE UNA BASE DE DATOS ######
def captura_DAVIS_Weewx(File, DB_FILE, N_DATOS, Param_4, ROOT, STATION, MailFROM, MailPASS, MailDEST):
    import sqlite3
    import time
    toolPreparaDir(File)

    def create_connection(FILE_DB):
        from sqlite3 import Error
        DBASE = None
        try:
            DBASE = sqlite3.connect(FILE_DB)
        except Error as e:
            print(e)
        return DBASE

    DBASE = create_connection(DB_FILE)
    QUERY_DB = DBASE.cursor()
    QUERY_DB.execute(
        'SELECT dateTime, windDir, windGustDir, windSpeed, windGust, outTemp, outHumidity, pressure, rain, rainRate, radiation, UV, barometer, inTemp, inHumidity, consBatteryVoltage, txBatteryStatus FROM archive ORDER BY dateTime DESC limit ' + N_DATOS)
    DATOS = QUERY_DB.fetchall()
    for LINEA in reversed(DATOS):
        TIME = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(LINEA[0]))
        if (LINEA[1] == None):
            WDIR = 'NaN'
        else:
            WDIR = str('%3.0f' % round(LINEA[1], 0))
        if (LINEA[2] == None):
            WGDR = 'NaN'
        else:
            WGDR = str('%3.0f' % round(LINEA[2], 0))
        #    WSPE = (float(LINEA[3])*1.609)                   # Conversion de mph a Km/h
        WSPE = (float(LINEA[3]) * 0.44704)  # Conversion de mph a m/s
        WSPE = str('%4.1f' % WSPE)
        #    WGUS = (float(LINEA[4])*1.609)                   # Conversion de mph a Km/h
        WGUS = (float(LINEA[4]) * 0.44704)  # Conversion de mph a m/s
        WGUS = str('%4.1f' % WGUS)
        TEMP = str('%4.1f' % round((LINEA[5] - 32) / 1.8, 2))  # Conversion de farenheit a centigrado
        #    TEMP = str('%.1f' % LINEA[5])
        HUME = str('%5.1f' % LINEA[6])
        APRE = (float(LINEA[7]) * 33.86389)  # Conversion de inhg a hectopascales
        APRE = str('%6.1f' % APRE)
        RAIN = str('%4.1f' % LINEA[8])
        RRAT = str('%4.1f' % LINEA[9])
        RAD = str('%6.1f' % LINEA[10])
        UV = str('%5.1f' % LINEA[11])
        APSL = (float(LINEA[12]) * 33.86389)  # Conversion de inhg a hectopascales
        APSL = str('%6.1f' % APSL)
        IN_TEMP = str('%4.1f' % round((LINEA[13] - 32) / 1.8, 2))  # Conversion de farenheit a centigrado
        IN_HUME = str('%5.1f' % LINEA[14])
        BVOL = str('%4.1f' % LINEA[15])
        BTXS = str('%1.0f' % LINEA[16])
        DATALINE = TIME + ' | ORO,Dm=' + WDIR + 'D,Dx=' + WGDR + 'D,Sm=' + WSPE + 'M,Sx=' + WGUS + 'M,Ta=' + TEMP + 'C,Ua=' + HUME + '%,Pa=' + APRE + 'H,Rc=' + RAIN + 'M,Rr=' + RRAT + 's,Ra=' + RAD + 'X,UV=' + UV + 'X | IN_Ta=' + IN_TEMP + 'C,IN_Ha=' + IN_HUME + '% SL_Pa=' + APSL + 'H BVol=' + BVOL + 'V BAT_TX_Stat=' + BTXS + ' \n'
        #    print (DATALINE)
        FileInput = open(File, 'a')
        FileInput.write('%s' % DATALINE)
        FileInput.close()


########################################################################################################################
#
#
#
# ENVIO DE DATOS
########################################################################################################################
########################################################################################################################
#
# 31-envioDatos: FUNCION PARA ENVIO DE DATOS################################
def envioDatos(TIPO, INFO):
    import os
    ###INI: Obtiene la informacion de la estacion###
    STATION, ROOT, PORTAL, PUERTO, USER, DR_DEST, M_FROM, M_PASS, M_DEST, CADA, N_INSTR, INSTR, INSTR_TYPE, INSTR_ID, \
    Param_1, Param_2, Param_3, Param_4, LINES, FileInput = leeInfo(INFO)
    ###FIN: Obtiene la informacion de la estacion###

    ###INI: Acciones del envio diario###
    if TIPO == 'Day':
        # Accion 1: Reinicio del script de captura de datos
        command = ROOT + 'Station/scripts/capturaReinicia.sh'
        if os.path.isfile(command):
            os.system(command)
        else:
            text = 'No se encuentra el fichero capturaReinicia.sh en ' + command
            print(text)
            text = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_' + TIPO + '_Reinicio. ' + text
            toolAnyadeLog(ROOT, STATION, 'ERROR', text, M_FROM, M_PASS, M_DEST)
        #########
        for n in range(N_INSTR):
            # Accion 2: Para cada instrumento, realiza la preparacion de los ficheros a enviar
            if (INSTR_TYPE[n] == 'CAM' or INSTR_TYPE == 'PiCAM'):
                text = 'El instrumento ' + INSTR[n] + \
                       ' es una camara con envio FTP. No se ejecuta ninguna accion para este Tipo. Tipo= "' + TIPO + '"'
                print(text)
                text = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_Envia_' + TIPO + '. ' + text
                toolAnyadeLog(ROOT, STATION, 'LOG', text, M_FROM, M_PASS, M_DEST)
            else:
                resultado = envioPreparaDia(ROOT, STATION, INSTR[n], INSTR_ID[n], TIPO)
                #########
                # Accion 3: Envia los datos si el RESULTADO es satisfactorio
                if (resultado == 'CONTINUA'):
                    envioEnvia(ROOT, STATION, INSTR[n], USER, PORTAL, PUERTO, DR_DEST, 'rawArchiveFTP', 'rawArchive',
                               TIPO, M_FROM, M_PASS, M_DEST)
                #########
                # Accion 4: Si no se han podido prepar los datos, se intenta enviar todos los archivos que haya preparados y se genera un mensaje de error
                else:
                    envioEnvia(ROOT, STATION, INSTR[n], USER, PORTAL, PUERTO, DR_DEST, 'rawArchiveFTP', 'rawArchive',
                               TIPO, M_FROM, M_PASS, M_DEST)
                    text = resultado
                    print(text)
                    text = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_' + TIPO + '. ' + text
                    toolAnyadeLog(ROOT, STATION, 'ERROR', text, M_FROM, M_PASS, M_DEST)
                    #########
    ###FIN: Acciones del envio diario###

    ###INI: Acciones del envio 10min###
    elif TIPO == '10min':
        # Accion 1: Prepara los ficheros de datos de los ultimos 10min
        for n in range(N_INSTR):
            if (INSTR_TYPE[n] == 'CAM' or INSTR_TYPE[n] == 'PiCAM'):
                resultado = envioPreparaCAM(ROOT, STATION, INSTR[n], INSTR_ID[n], TIPO)
            else:
                resultado = envioPrepara(ROOT, STATION, INSTR[n], INSTR_ID[n], LINES[n], TIPO)
            #########

            # Accion 2: Envia los datos si el RESULTADO es satisfactorio
            if resultado == 'CONTINUA':
                envioEnvia(ROOT, STATION, INSTR[n], USER, PORTAL, PUERTO, DR_DEST, 'rawFTP', 'rawInput', TIPO, M_FROM,
                           M_PASS, M_DEST)
            #########
            # Accion 3: Si no se han podido prepar los datos, se intenta enviar todos los archivos que haya preparados y se genera un mensaje de error
            else:
                envioEnvia(ROOT, STATION, INSTR[n], USER, PORTAL, PUERTO, DR_DEST, 'rawFTP', 'rawInput', TIPO, M_FROM,
                           M_PASS, M_DEST)
                text = resultado
                print(text)
                text = toolInstant(
                    '%Y-%m-%d %H:%M:%S') + ' | ERROR_' + TIPO + '. Ha habido errores en el envío de algunos ficheros. Error: ' + text
                toolAnyadeLog(ROOT, STATION, 'ERROR', text, M_FROM, M_PASS, M_DEST)
    #########
    ###FIN: Acciones del envio 10min###

    ###INI: Acciones del envio SISMO_1min###
    elif TIPO == 'SISMO_1min':
        # Accion 1: Localiza y lee la informacion SISMO
        sismo = os.path.dirname(os.path.abspath(__file__)) + '/sismo.txt'
        if os.path.isfile(sismo):
            SIS_STATION, SIS_ROOT, SIS_PORTAL, SIS_PUERTO, SIS_USER, SIS_DR_DEST, SIS_M_FROM, SIS_M_PASS, CADA, \
            SIS_M_DEST, SIS_N_INSTR, SIS_INSTR, SIS_INSTR_TYPE, SIS_INSTR_ID, SIS_Param_1, SIS_Param_2, SIS_Param_3, \
            SIS_Param_4, SIS_LINES, FileInput = leeInfo(sismo)
            #########
            # Accion 2: Prepara los ficheros de datos de los ultimo min
            for n in range(SIS_N_INSTR):
                if SIS_INSTR_TYPE[n] == 'CAM':
                    resultado = envioPreparaCAM(SIS_ROOT, SIS_STATION, SIS_INSTR[n], SIS_INSTR_ID[n], TIPO)
                else:
                    resultado = envioPrepara(SIS_ROOT, SIS_STATION, SIS_INSTR[n], SIS_INSTR_ID[n], SIS_LINES[n], TIPO)
                #########
                # Accion 2: Envia los datos si el RESULTADO es satisfactorio
                if resultado == 'CONTINUA':
                    envioEnvia(SIS_ROOT, SIS_STATION, SIS_INSTR[n], SIS_USER, SIS_PORTAL, SIS_PUERTO, SIS_DR_DEST,
                               'rawSISMO', '', TIPO, SIS_M_FROM, SIS_M_PASS, SIS_M_DEST)
                #########
                # Accion 3: Si no se han podido prepar los datos, se intenta enviar todos los archivos que haya preparados y se genera un mensaje de error
                else:
                    envioEnvia(SIS_ROOT, SIS_STATION, SIS_INSTR[n], SIS_USER, SIS_PORTAL, SIS_PUERTO, SIS_DR_DEST,
                               'rawSISMO', '', TIPO, SIS_M_FROM, SIS_M_PASS, SIS_M_DEST)
                    text = resultado
                    print(text)
                    text = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_' + TIPO + '. ' + text
                    toolAnyadeLog(ROOT, STATION, 'ERROR', text, M_FROM, M_PASS, M_DEST)
        #########
        # Accion 4: Si no existe el fichero sismo.txt se genera un mensaje de error
        else:
            text = 'No se encientra el fichero sismo.txt en el sistema. No puede realizarse ninguna accion para este tipo. Tipo= "' + TIPO + '"'
            print(text)
            text = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_Envio. ' + text
            toolAnyadeLog(ROOT, STATION, 'ERROR', text, M_FROM, M_PASS, M_DEST)
    ##########
    ###FIN: Acciones del envio SISMO_1min###

    ###INI: Acciones del envio rawData###
    elif TIPO == 'rawData':
        for n in range(N_INSTR):
            # Accion 1: Envia los datos almacenados en las carpetas rawArchiveFTP y rawFTP
            envioEnvia(ROOT, STATION, INSTR[n], USER, PORTAL, PUERTO, DR_DEST, 'rawArchiveFTP', 'rawArchive', TIPO,
                       M_FROM, M_PASS, M_DEST)
            envioEnvia(ROOT, STATION, INSTR[n], USER, PORTAL, PUERTO, DR_DEST, 'rawFTP', 'rawInput', TIPO, M_FROM,
                       M_PASS, M_DEST)
        text = 'Se ejecuta el script de envio de datos con el tipo "' + TIPO + '"'
        print(text)
        text = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_Envia_' + TIPO + '. ' + text
        toolAnyadeLog(ROOT, STATION, 'LOG', text, M_FROM, M_PASS, M_DEST)
    #########
    ###FIN: Acciones del envio rawData###

    ###INI: Acciones del envio CAM###
    elif TIPO == 'CAM':
        # Accion 1: Prepara los ficheros de datos de los ultimos 10min
        for n in range(N_INSTR):
            if INSTR_TYPE[n] == 'CAM':
                resultado = envioPreparaCAM(ROOT, STATION, INSTR[n], INSTR_ID[n], TIPO)
                # Accion 2: Envia los datos si el RESULTADO es satisfactorio
                if resultado == 'CONTINUA':
                    envioEnvia(ROOT, STATION, INSTR[n], USER, PORTAL, PUERTO, DR_DEST, 'rawFTP', 'rawInput', TIPO,
                               M_FROM, M_PASS, M_DEST)
                #########
                # Accion 3: Si no se han podido prepar los datos, se intenta enviar todos los archivos que haya preparados y se genera un mensaje de error
                else:
                    envioEnvia(ROOT, STATION, INSTR[n], USER, PORTAL, PUERTO, DR_DEST, 'rawFTP', 'rawInput', TIPO,
                               M_FROM, M_PASS, M_DEST)
                    texto = resultado
                    print(texto)
                    texto = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_' + TIPO + '. ' + texto
                    toolAnyadeLog(ROOT, STATION, 'ERROR', TEXT, M_FROM, M_PASS, M_DEST)
            #########
            else:
                TEXT = 'El instrumento ' + INSTR[
                    n] + ' no es una camara. No se ejecuta ningina accion para este Tipo. Tipo= "' + TIPO + '"'
                print(TEXT)
                texto = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_Envia_' + TIPO + '. ' + TEXT
                toolAnyadeLog(ROOT, STATION, 'LOG', texto, M_FROM, M_PASS, M_DEST)
    #########
    ###FIN: Acciones del envio CAM###

    ###INI: Acciones del envio USB###
    elif TIPO == 'USB':
        import psutil
        # Accion 1: Preparo la unidad USB
        if not (os.path.isdir('/mnt/USB')):
            command = ('sudo mkdir /mnt/USB')
            os.system(command)
        command = ('sudo umount /mnt/USB')
        os.system(command)
        command = ('sudo mount /dev/sda1 /mnt/USB')
        resultado = os.system(command)
        #########
        if resultado == 0:
            # print ('Resultado= "'+str(RESULTADO)+'"')
            # Accion 2: Comprueba si hay suficiene espacio en disco
            size = toolGetSize(ROOT + STATION)
            disp = psutil.disk_usage('/mnt/USB')
            size_usb = toolGetSize('/mnt/USB/' + STATION)
            # print ('Espacio ocupado por Station   : '+str(SIZE))
            # print ('Espacio disponible en /mnt/USB: '+str(DISP[2]))
            # print ('Espacio ocupado por Station en /mnt/USB: '+str(SIZE_USB))
            disp_total = disp[2] + size_usb
            if (size > disp_total):
                text = 'No hay espacio suficiente en el USB para realizar la copia. Disponible en USB= ' + str(
                    disp_total) + 'bytes Espacio ocupado por ' + ROOT + STATION + '= ' + str(size) + 'bytes'
                print(text)
                text = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_' + TIPO + '. ' + text
                toolAnyadeLog(ROOT, STATION, 'ERROR', text, M_FROM, M_PASS, M_DEST)
                command = ('sudo umount /mnt/USB')
                os.system(command)
            else:
                ##########
                # Accion 3: Si se ha encontrado la menoria USB y hay espacio suficuente se realiza el rsync
                command = 'sudo rsync  -r ' + ROOT + STATION + ' /mnt/USB/'
                os.system(command)
                text = 'La copia al USB se ha realizado con exito'
                print(text)
                text = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_' + TIPO + '. ' + text
                toolAnyadeLog(ROOT, STATION, 'LOG', text, M_FROM, M_PASS, M_DEST)
                command = ('sudo umount /mnt/USB')
                os.system(command)
        #########
        # Accion 4: Si no se ha encontrado la menoria USB se genera un mensaje de error
        else:
            text = 'No se ha podido montart el dispositivo USB. Resultado= "' + str(resultado) + '"'
            print(text)
            text = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_' + TIPO + '. ' + text
            toolAnyadeLog(ROOT, STATION, 'ERROR', text, M_FROM, M_PASS, M_DEST)
    #########
    ###FIN: Acciones del envio USB###

    ###INI: Acciones en caso de que el TIPO no este definido###
    else:
        text = 'El TIPO de envio "' + TIPO + '" no esta definido en el sistema'
        print(text)
        text = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_Envio. ' + text

        toolAnyadeLog(ROOT, STATION, 'ERROR', text, M_FROM, M_PASS, M_DEST)
    ###FIN: Acciones en caso de que el TIPO no este definido###


###############################################################################
# %%
#
# 32-envioPrepara: FUNCION PARA PREPARAR LOS FICHEROS DE 10MIN################
def envioPrepara(ROOT, STATION, INSTRUMENT, INSTRUMENT_ID, LINES, TIPO):
    import os
    import time
    # DEFINE LOS FICHEROS A TRATAR
    FILE = time.strftime('%Y%m%d') + '.ail'
    FICHERO_IN = ROOT + 'Station/' + INSTRUMENT + '/rawInput/' + FILE

    # PREPARA LA RUTA DE LOS FICHEROS; DATOS Y ULTIMO DATO ENVIADO
    if (TIPO == 'SISMO_1min'):
        FICHERO_OUT = ROOT + 'Station/' + INSTRUMENT + '/rawSISMO/RT_SISMO_1min_' + \
                      toolInstant('%Y%m%d%H%M%S') + '_' + STATION + '-' + INSTRUMENT_ID + '.ail'
        toolPreparaDir(FICHERO_OUT)
        FICHERO_LAST = ROOT + 'Station/scripts/logs/LastPrep_SISMO-' + INSTRUMENT + '.log'
        toolPreparaDir(FICHERO_LAST)
    else:
        FICHERO_OUT = ROOT + 'Station/' + INSTRUMENT + '/rawFTP/RT_10min_' + \
                      toolInstant('%Y%m%d%H%M%S') + '_' + STATION + '-' + INSTRUMENT_ID + '.ail'
        toolPreparaDir(FICHERO_OUT)
        FICHERO_LAST = ROOT + 'Station/scripts/logs/LastPrep-' + INSTRUMENT + '.log'
        toolPreparaDir(FICHERO_LAST)

    if (os.path.exists(FICHERO_IN)):
        # LEE EL UTLIMO DATO REGISTRADO LastRead Y EL ULTIMO DATO ENVIADO LastStor
        if (os.path.getsize(FICHERO_IN) != 0):
            DataFile = open(FICHERO_IN, "r")
            LastRead = DataFile.readlines()[-1]
            DataFile.close()
        if (os.path.exists(FICHERO_LAST)):
            DataFile = open(FICHERO_LAST, "r")
            LastStor = DataFile.readlines()[-1]
            DataFile.close()
        else:
            LastStor = ''
        # print ('No hay datos previos')

        if (LastRead != LastStor):
            COMMAND = 'tail -' + str(LINES) + ' ' + FICHERO_IN + ' > ' + FICHERO_OUT
            os.system(COMMAND)
            COMMAND_2 = 'tail -1 ' + FICHERO_IN + ' > ' + FICHERO_LAST
            os.system(COMMAND_2)
            return 'CONTINUA'
        else:
            TEXT = 'El fichero ' + FILE + ' del instrumento ' + INSTRUMENT + ' no dispone de nuevos datos desde su anterior preparacion'
            return TEXT
    else:
        TEXT = 'Del instrumento ' + INSTRUMENT + ' no existe el fichero: ' + FILE
        return TEXT


###############################################################################
#
#
# 33-envioPreparaDia: FUNCION PARA PREPARAR LOS FICHEROS DIARIOS##############
def envioPreparaDia(ROOT, STATION, INSTRUMENT, INSTRUMENT_ID, TIPO):
    import os
    from datetime import date, timedelta
    # print 'Entra en preparaDia'
    ayer = date.today() - timedelta(1)
    ayer = ayer.strftime('%Y%m%d')
    toolCompruebaFolder(ROOT + 'Station/' + INSTRUMENT + '/rawFTP/')
    toolCompruebaFolder(ROOT + 'Station/' + INSTRUMENT + '/rawArchive/')
    toolCompruebaFolder(ROOT + 'Station/' + INSTRUMENT + '/rawArchiveFTP/')

    fichero_ayer = ROOT + 'Station/' + INSTRUMENT + '/rawInput/' + ayer + '.ail'
    fichero_ftp = ROOT + 'Station/' + INSTRUMENT + '/rawFTP/RT_Day_' + ayer + '_' + STATION + '-' + INSTRUMENT_ID + '.ail'
    fichero_arc = ROOT + 'Station/' + INSTRUMENT + '/rawArchive/RT_Day_' + ayer + '_' + STATION + '-' + INSTRUMENT_ID + '.ail'
    fichero_arcftp = ROOT + 'Station/' + INSTRUMENT + '/rawArchiveFTP/RT_Day_' + ayer + '_' + STATION + '-' + INSTRUMENT_ID + '.ail'
    if (os.path.exists(fichero_ayer)):
        # print 'el fichero existe. CONTINUA'
        command_1 = 'mv ' + fichero_ayer + ' ' + fichero_arc
        command_2 = 'cp ' + fichero_arc + ' ' + fichero_ftp
        command_3 = 'cp ' + fichero_arc + ' ' + fichero_arcftp
        text = toolInstant('%Y-%m-%d %H:%M:%S') + \
               ' | LOG_' + TIPO + '. Se mueve el fichero: ' + ayer + '.ail del instrumento ' + INSTRUMENT + ' a ' + fichero_arc
        toolAnyadeLog(ROOT, STATION, 'LOG', text, 'from', 'pass', 'to')

        os.system(command_1)
        os.system(command_2)
        os.system(command_3)
        return 'CONTINUA'
    else:
        text = 'Del instrumento ' + INSTRUMENT + ' no existe el fichero de ayer: ' + ayer + '.ail'
        return text


########################################################################
#
#
# 34-envioPreparaCAM: FUNCION PARA PREPARAR LOS FICHEROS DE CAMARAS#############
def envioPreparaCAM(ROOT, STATION, INSTRUMENT, INSTRUMENT_ID, TIPO):
    import os
    # Variable para la ruta al directorio
    DIR_JPG = ROOT + STATION + 'Station/' + INSTRUMENT + '/rawInput/'
    DIR_DEST = ROOT + STATION + 'Station/' + INSTRUMENT + '/rawFTP/'
    toolCompruebaFolder(DIR_DEST)
    DIR_ARCH = ROOT + STATION + 'Station/' + INSTRUMENT + '/rawArchive/'
    toolCompruebaFolder(DIR_ARCH)
    contador = 0

    # Lista con todos los ficheros del directorio:
    lstDir = os.walk(DIR_JPG)  # os.walk()Lista directorios y ficheros

    # Busca los ficheros jpg que existen en el directorio
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if extension == ".jpg":
                FICHERO_JPG = root + '/' + fichero
                contador = contador + 1
                # print (str(CONTADOR) + '    ' + FICHERO_JPG)
                command = 'cp ' + FICHERO_JPG + ' ' + DIR_ARCH
                os.system(command)
                command = 'mv ' + FICHERO_JPG + ' ' + DIR_DEST
                os.system(command)
                # print (OUT)
    if (contador > 0):
        return 'CONTINUA'
    else:
        text = ' | ERROR_' + INSTRUMENT + '. No hay imagenes de la camara ' + INSTRUMENT_ID
        return text


###############################################################################
# %%
#
# 35-envia FUNCION DE ENVIO DE DATOS#####################################
def envioEnvia(ROOT, STATION, INSTRUMENT, USER, PORTAL, PORT, DEST, FOLDER_ORIG, FOLDER_DEST, TIPO, FROM, PASS, TO):
    import glob
    import os
    origen = ROOT + 'Station/' + INSTRUMENT + '/' + FOLDER_ORIG + '/'
    listafichero = glob.glob(origen + '*')

    if TIPO == 'SISMO_1min':
        destino = USER + '@' + PORTAL + ':' + STATION + '/' + INSTRUMENT + '/' + FOLDER_DEST
    else:
        destino = USER + '@' + PORTAL + ':' + DEST + '/' + STATION + '/' + INSTRUMENT + '/' + FOLDER_DEST

    if INSTRUMENT[0:3] == 'CAM':
        # print('Envia cámaras')
        command = 'scp -P ' + PORT + ' ' + origen + '* ' + destino
        out = os.system(command)
        out = str(out)
        if out == '0':
            text = toolInstant('%Y-%m-%d %H:%M:%S') \
                   + ' | LOG_' + TIPO + '. Se ha realizado el envio de todas las imagenes que había en ' + origen
            toolAnyadeLog(ROOT, STATION, 'LOG', text, 'from', 'pass', 'to')
            command = 'rm ' + origen + '*'
            os.system(command)
        else:
            text = toolInstant('%Y-%m-%d %H:%M:%S') \
                   + ' | ERROR_' + TIPO + '. No ha sido posible realizar el envio de las imagenes que habia en ' + \
                   origen + '. Codigo: ' + str(out)
            toolAnyadeLog(ROOT, STATION, 'ERROR', text, FROM, PASS, TO)
    else:
        # print('Envia otras cosas')
        for fichero in listafichero:
            command = 'scp -P ' + PORT + ' ' + fichero + ' ' + destino
            # print(command)
            # print('Hace el envio del fichero '+fichero+' a la carpeta '+destino)
            #
            out = os.system(command)
            out = str(out)
            if out == '0':
                text = toolInstant('%Y-%m-%d %H:%M:%S') \
                       + ' | LOG_' + TIPO + '. Se ha realizado el envio del fichero: ' + fichero
                toolAnyadeLog(ROOT, STATION, 'LOG', text, 'from', 'pass', 'to')
                # print 'Envio correcto: '+OUT+' Procedo a borrar el archivo enviado'
                if (TIPO == 'rawArchiveFTP'):
                    command = 'cp ' + fichero + ' ' + ROOT + 'Station/' + INSTRUMENT + '/rawArchive'
                    # print(command)
                    os.system(command)
                else:
                    envioBorra(fichero)
            else:
                text = toolInstant('%Y-%m-%d %H:%M:%S') \
                       + ' | ERROR_' + TIPO + '. No ha sido posible realizar el envio del fichero: ' + fichero + '. Codigo: ' + out
                toolAnyadeLog(ROOT, STATION, 'ERROR', text, FROM, PASS, TO)


########################################################################
# %%
#
# 36-envioBorra_ FUNCION QUE BORRA LOS ARCHIVOS ENVIADOS######################
def envioBorra(FILE):
    import os
    command = 'rm ' + FILE
    # print 'Elimina el fichero'+FILE
    # print COMMAND
    os.system(command)


########################################################################
# %%
#
# 37-borraCAM: FUNCION DE BORRADO DE CAMARAS#############################
def envioBorraCAM(ROOT, STATION, INSTRUMENT, DIAS):
    import os, time
    ahora = time.time()
    n_files = 0
    for fichero in os.listdir(ROOT + 'Station/' + INSTRUMENT + '/rawArchive/'):
        este = os.path.join(ROOT + 'Station/' + INSTRUMENT + '/rawArchive/', fichero)
        if os.stat(este).st_mtime < ahora - (60 * 60 * 24 * int(DIAS)) and os.path.isfile(este):
            os.remove(este)
            n_files = n_files + 1
    text = 'Se han borrado ' + str(n_files) + ' imagenes de la camara ' \
           + INSTRUMENT + ' tomadas hace mas de ' + str(DIAS) + ' días'
    print(' ')
    print(text)
    text = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_CAM. ' + text
    toolAnyadeLog(ROOT, STATION, 'LOG', text, 'from', 'pass', 'to')


########################################################################
#
#
#
# MONITORIZACION
#
########################################################################################################################
########################################################################################################################
#
# 41-monitor:
def monitor(PROCESO, N_INST, CADA, ROOT, STATION, FROM, PASS, DEST):
    from time import sleep
    #    from threading import current_thread
    print('Se va a monitorizar el estado de funcionamiento de los subprocesos cada ' + str(CADA) + ' segundos')
    # print ('La estación tiene '+str(N_INST)+' instrumerntos configurados para adquisición de datos en "info.txt" ')
    flag = 1
    TIPO = 'MON'
    while (flag):
        CORRIENDO = compruebaSubprocesos(PROCESO)
        if (N_INST == int(CORRIENDO)):
            TEXT = toolInstant(
                '%Y-%m-%d %H:%M:%S') + ' | Hay ' + CORRIENDO + ' subprocesos de -' + PROCESO + '- en ejecución. Todo en orden.'
            print(TEXT)
            TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_MONITOR. ' + TEXT
            toolAnyadeLog(ROOT, STATION, TIPO, TEXT, FROM, PASS, DEST)
        else:
            TEXT = toolInstant(
                '%Y-%m-%d %H:%M:%S') + ' | Houston, tenemos un problema. Hay algún proceso que se ha parado.'
            print(TEXT)
            TIPO = 'ERROR'
            TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_MONITOR. ' + TEXT
            toolAnyadeLog(ROOT, STATION, TIPO, TEXT, FROM, PASS, DEST)
        sleep(CADA)


########################################################################
#
#
# 42-compruebaSubprocesos: FUNCION PARA COMPROBAR SI UN PROCESO ESTA EN FUNCIONAMIENTO. DEVUELVE EL NUMERO DE PROCESOS EN EJECUCION #####
def compruebaSubprocesos(PROCESO):
    import subprocess
    # PROCESO = 'pythonCaptura'
    COMMAND = 'ps ax | grep -v grep | grep ' + PROCESO
    OUT = str(subprocess.check_output(COMMAND, shell=True))

    IN = OUT.find("'")
    EN = OUT.find(" ", IN + 4)
    PID = OUT[IN + 1:EN]

    # print ('OUT='+OUT)
    # print ('IN='+str(IN))
    # print ('EN='+str(EN))
    # print ('PROCESO_ID= '+PID)
    # print ()

    COMMAND = 'ps huH p ' + PID + ' | wc -l'
    OUT = str(subprocess.check_output(COMMAND, shell=True))
    IN = OUT.find("'")
    EN = OUT.find("'", IN + 1)
    N_PROC = str(int(OUT[IN + 1:EN - 2]) - 2)
    # print ('OUT='+OUT)
    # print ('IN='+str(IN))
    # print ('EN='+str(EN))
    # print ('N_SUBPROCESOS= '+N_PROC)
    return N_PROC


########################################################################
# 43-compruebaRecepcion####
def compruebaRecepcion(DIRLOCAL, EST_TIPO, EST_NAME, INST_NAME, CADA, FROM, PASS, TO):
    import os
    import pathlib
    from datetime import datetime, timedelta

    print('  **Comprobando la recepción de datos del instrumento ' + INST_NAME)
    DATAFOLDER = DIRLOCAL + EST_TIPO + '/' + EST_NAME + '/' + INST_NAME
    FILESINFOLDER = [arch.name for arch in sorted(pathlib.Path(DATAFOLDER).iterdir(), key=os.path.getmtime) if
                     arch.is_file()]
    if (not FILESINFOLDER):
        TEXT = '-' + EST_NAME + '-' + INST_NAME + '- No se encuentran ficheros el directorio de recepción de datos.'
        # print (TEXT)
        TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_Reception. ' + TEXT
        toolAnyadeLog(DIRLOCAL, '', 'ERROR', TEXT, FROM, PASS, TO)
        RESULTADO = 'PROBLEM'
    else:
        ULTFILE = FILESINFOLDER[len(FILESINFOLDER) - 1]
        # print ('      El último fichero recibido es: '+ULTFILE)
        ULTFILE = DATAFOLDER + '/' + ULTFILE
        AHORA = datetime.now()
        MAXDELAY = AHORA - timedelta(minutes=int(CADA))
        # print ('         Ahora = '+str(AHORA))
        # print ('      maxDelay = '+str(MAXDELAY))

        FNAME = pathlib.Path(ULTFILE)
        FTIME = datetime.fromtimestamp(FNAME.stat().st_mtime)
        # print('      fileTime = '+str(FTIME))
        if (MAXDELAY > FTIME):
            TEXT = '-' + EST_NAME + '-' + INST_NAME + '- El último fichero recibido es demasiado antuguo: Fichero ' + ULTFILE
            # print (TEXT)
            TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_Reception. ' + TEXT
            toolAnyadeLog(DIRLOCAL, '', 'ERROR', TEXT, FROM, PASS, TO)
            RESULTADO = 'PROBLEM'
        else:
            TEXT = '-' + EST_NAME + '-' + INST_NAME + '- Fichero recibido en el momento esperado.'
            # print (TEXT)
            TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_Reception. ' + TEXT
            toolAnyadeLog(DIRLOCAL, '', 'LOG', TEXT, FROM, PASS, TO)
            RESULTADO = 'OK'
            compruebaAnteriorProblema(DIRLOCAL, EST_NAME, INST_NAME, FROM, PASS, TO)

    return RESULTADO


##########################################################################
# %%
#
# 44-compruebaPosicion:
def compruebaPosicion(DIRLOCAL, STATION, FECHA, DIST, UMBRAL, FROM, PASS, TO):
    if (DIST > UMBRAL):
        TEXT = toolInstant(
            '%Y-%m-%d %H:%M:%S') + ' | LA BOYA -' + STATION + '- SE HA ALEJADO DEMASIADO DE SU POSICIÓN en el mensaje recibido en ' + FECHA + '. *Umbral= ' + str(
            UMBRAL) + 'm Distancia= ' + str(DIST) + 'm*'
        toolAnyadeLog(DIRLOCAL, '', 'ERROR', TEXT, FROM, PASS, TO)
        TEXT = '*LA BOYA -\033[1;93m' + STATION + '\033[0m- SE HA ALEJADO DEMASIADO DE SU POSICIÓN en el mensaje recibido en ' + FECHA + '. *Umbral= \033[1;93m' + str(
            UMBRAL) + 'm\033[0m Distancia= \033[1;31m' + str(DIST) + '\033[0;mm*'
    else:
        TEXT = 'ACTUAL POSICIÓN. Todo en orden en los datos de ' + FECHA + ' *Umbral= ' + str(
            UMBRAL) + 'm  Distancia= ' + str(DIST) + 'm* '
        TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_' + STATION + '. ' + TEXT
        toolAnyadeLog(DIRLOCAL, '', 'LOG', TEXT, FROM, PASS, TO)
        TEXT = 'ACTUAL POSICIÓN. Todo en orden en los datos de \033[1;93m' + FECHA + '\033[0m *Umbral= \033[1;93m' + str(
            UMBRAL) + 'm \033[0;m Distancia= \033[1;93m' + str(DIST) + 'm\033[0m* '
    return TEXT


##########################################################################
#
#
# 45-compruebaVoltaje
def compruebaVoltaje(DIRLOCAL, STATION, FECHA, VOLT, UMBRAL, FROM, PASS, TO):
    if (VOLT < UMBRAL):
        TEXT = toolInstant(
            '%Y-%m-%d %H:%M:%S') + ' | EL VOLTAJE EN -' + STATION + '- ES DEMASIADO BAJO. Mensaje recibido en ' + FECHA + '. *Umbral= ' + str(
            UMBRAL) + 'V Voltaje= ' + str(VOLT) + 'V*'
        toolAnyadeLog(DIRLOCAL, '', 'ERROR', TEXT, FROM, PASS, TO)
        TEXT = '*EL VOLTAJE EN -\033[1;31m' + STATION + '\033[0;m- ES DEMASIADO BAJO. Mensaje recibido en ' + FECHA + '. *Umbral= \033[1;93m' + str(
            UMBRAL) + 'V\033[0;m Voltaje= \033[1;31m' + str(VOLT) + 'V\033[0;m*'
    else:
        TEXT = 'BATERÍA VOLTAJE. Todo en orden en los datos de ' + FECHA + ' *Umbral= ' + str(
            UMBRAL) + 'V   Voltaje= ' + str(VOLT) + 'V* '
        TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_' + STATION + '. ' + TEXT
        toolAnyadeLog(DIRLOCAL, '', 'LOG', TEXT, FROM, PASS, TO)
        TEXT = 'BATERÍA VOLTAJE. Todo en orden en los datos de \033[1;93m' + FECHA + '\033[0m *Umbral= \033[1;93m' + str(
            UMBRAL) + 'V\033[0;m   Voltaje= \033[1;93m' + str(VOLT) + 'V\033[0;m* '
    return TEXT


##############################################################################
#
#
# 46-compruebaTemperatura
def compruebaTemperatura(DIRLOCAL, STATION, FECHA, TEMP, UMBRAL, FROM, PASS, TO):
    if (TEMP > UMBRAL):
        TEXT = toolInstant(
            '%Y-%m-%d %H:%M:%S') + ' | LA TEMPERATURA EN -' + STATION + '- ES DEMASIADO ALTA en el mensaje recibido en ' + FECHA + '. *Umbral= ' + str(
            UMBRAL) + ' Temperatura= ' + str(TEMP) + 'ºC*'
        toolAnyadeLog(DIRLOCAL, '', 'ERROR', TEXT, FROM, PASS, TO)
        TEXT = '*LA TEMPERATURA EN -' + STATION + '- ES DEMASIADO ALTA en el mensaje recibido en ' + FECHA + '. *Umbral= \033[1;93m' + str(
            UMBRAL) + '\033[0; Temperatura= \033[1;93m' + str(TEMP) + 'ºC\033[0;*'
    else:
        TEXT = 'DL. TEMPERATURA. Todo en orden en los datos de ' + FECHA + ' *Umbral= ' + str(
            UMBRAL) + 'ºC  Temperatura= ' + str(TEMP) + 'ºC* '
        TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_' + STATION + '. ' + TEXT
        toolAnyadeLog(DIRLOCAL, '', 'LOG', TEXT, FROM, PASS, TO)
        TEXT = 'DL. TEMPERATURA. Todo en orden en los datos de \033[1;93m' + FECHA + '\033[0m *Umbral= \033[1;93m' + str(
            UMBRAL) + 'ºC\033[0;m  Temperatura= \033[1;93m' + str(TEMP) + 'ºC\033[0;m* '
    return TEXT


###############################################################################
#
#
# 47-compruebaAnteriorProblema####
def compruebaAnteriorProblema(DIRLOCAL, EST_NAME, INST_NAME, FROM, PASS, TO):
    import os
    from datetime import datetime, timedelta
    ULTIMO = []
    FIL_MAIL = DIRLOCAL + 'scripts/logs/MAIL-DataReception.log'
    FIL_TMP = DIRLOCAL + 'scripts/logs/TMP.log'
    EST_INST = EST_NAME + '-' + INST_NAME
    if os.path.isfile(FIL_MAIL):
        file = open(FIL_MAIL, 'r')
        file_tmp = open(FIL_TMP, 'w')
        for line in file:
            if (line[:line.find(' |')] == EST_INST):
                ULTIMO = line[line.find(' |') + 3:]
            else:
                file_tmp.write(line)
        file.close()
        file_tmp.close()
        COMMAND = 'rm ' + FIL_MAIL
        os.system(COMMAND)
        COMMAND = 'mv ' + FIL_TMP + ' ' + FIL_MAIL
        os.system(COMMAND)
    if (ULTIMO):
        ULTIMO = datetime(int(ULTIMO[0:4]), int(ULTIMO[6:7]), int(ULTIMO[9:10]), int(ULTIMO[12:13]), int(ULTIMO[15:16]),
                          int(ULTIMO[17:18]))
        HACE24 = ULTIMO - timedelta(hours=24)
        if (ULTIMO > HACE24):
            print('El últomo problema es de hace menos de 24h')
            TEXT = 'Se vuelven a recibir mensajes del instrumento ' + INST_NAME + ' en la estación ' + EST_NAME
            SUBJET = 'Recuperación del instrumento ' + INST_NAME + ' en la estación ' + EST_NAME
            toolSendMail(FROM, PASS, TO, SUBJET, TEXT)
            toolAnyadeLog(DIRLOCAL, '', 'LOG', TEXT, FROM, PASS, TO)


###############################################################################
#
#
# 48-compruebaUltimio####
def compruebaUltimo(DIRLOCAL, DATAFOLDER, FILESINFOLDER, EST_NAME, CADA, FROM, PASS, TO):
    from datetime import datetime, timedelta
    import pathlib

    ULTFILE = FILESINFOLDER[len(FILESINFOLDER) - 1]
    # print ('      El último fichero recibido es: '+ULTFILE)
    ULTFILE = DATAFOLDER + '/' + ULTFILE
    AHORA = datetime.now()
    MAXDELAY = AHORA - timedelta(minutes=int(CADA))
    # print ('         Ahora = '+str(AHORA))
    # print ('      maxDelay = '+str(MAXDELAY))

    FNAME = pathlib.Path(ULTFILE)
    FTIME = datetime.fromtimestamp(FNAME.stat().st_mtime)
    # print('      fileTime = '+str(FTIME))
    if (MAXDELAY > FTIME):
        TEXT = '-' + EST_NAME + '- El último fichero recibido es demasiado antuguo: Fichero ' + ULTFILE
        # print (TEXT)
        TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_' + EST_NAME + '. ' + TEXT
        toolAnyadeLog(DIRLOCAL, '', 'ERROR', TEXT, FROM, PASS, TO)
        RESULTADO = 'PROBLEM'
    else:
        TEXT = 'Fichero recibido en el momento esperado.'
        print(TEXT)
        TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_' + EST_NAME + '. ' + TEXT
        toolAnyadeLog(DIRLOCAL, '', 'LOG', TEXT, FROM, PASS, TO)
        compruebaAnteriorProblema(DIRLOCAL, EST_NAME, EST_NAME, FROM, PASS, TO)
        RESULTADO = 'CORRECTO'
    return RESULTADO


########################################################################
#
#
#
# TOOLS
#
########################################################################################################################
########################################################################################################################
#
#
# 61-toolInstant: FUNCION DE CALCULO DEL INSTANTE###############################
def toolInstant(FORMAT):
    from time import strftime
    return strftime(FORMAT)


###############################################################################
#
#
# 62-toolHaversie: FUNCIÓN PARA CALCULAR DISTANCIA ENTRE DOS PUNTOS #########
def toolHaversine(lat1, lon1, lat2, lon2):
    import math
    rad = math.pi / 180
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    R = 6372.795477598
    a = (math.sin(rad * dlat / 2)) ** 2 + math.cos(rad * lat1) * math.cos(rad * lat2) * (math.sin(rad * dlon / 2)) ** 2
    distancia = 2 * R * math.asin(math.sqrt(a)) * 1000
    return distancia


###############################################################################
#
#
# 63-toolGetSize : FUNCION PARA CALCULAR EL ESPACIO OCUPADO ####################
def toolGetSize(PATH):
    import os
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(PATH):
        for f in filenames:
            file_size = os.path.join(dirpath, f)
            total_size += os.path.getsize(file_size)
    return total_size


###############################################################################
#
#
# 64-toolSendMail_ FUNCION PARA ENVIO DE CORREOS ELECTRONICOS###################
def toolSendMail(FROM, PASS, DEST, SUBJET, TEXT):
    import os
    import smtplib
    import email.mime.text

    if (FROM == ' ' or PASS == ' ' or DEST == ' '):
        print(' ')
        print(' ---- NO ES POSIBLE ENVIAR EL CORREO DE NOTIFICACION. FALTAN DATOS ---')
        print(' ')
    else:
        IP = os.popen('curl canhazip.com').read()
        if os.path.isfile('/proc/sys/kernel/hostname'):
            HOST = os.popen('cat /proc/sys/kernel/hostname').read()
        else:
            HOST = 'Unknown host'

        TEXT = TEXT + '\n______________________________\nEnviado desde: ' + str(HOST) + '       IP WAN: ' + str(IP)
        msg = email.mime.text.MIMEText(TEXT)
        msg['Subject'] = SUBJET
        msg['From'] = FROM
        msg['To'] = DEST
        DEST = DEST.split(',')
        s = smtplib.SMTP_SSL('smtp.gmail.com', '465')
        s.login(FROM, PASS)
        s.sendmail(FROM, DEST, msg.as_string())
        s.quit()


###############################################################################
#
#
# 65-anyadeLog: FUNCION DE ANYADIR LINEA AL LOG#################################
def toolAnyadeLog(ROOT, STATION, TIPO, TEXT, FROM, PASS, DEST):
    horas = 3
    toolCompruebaFolder(ROOT + 'Station/scripts/logs/')
    # fichero = ROOT + 'Station/scripts/logs/' + TIPO + '-' + STATION + '.log'

    if TIPO != 'SPE':
        fichero = ROOT + 'Station/scripts/logs/' + TIPO + '-Station.log'
        file = open(fichero, 'a+')
        file.write(TEXT + '\n')
        file.close()
        toolMantenerTamanyoLog(fichero)
    else:
        fichero = ROOT + 'Station/scripts/logs/LOG-Station.log'
        file = open(fichero, 'a+')
        file.write(TEXT + '\n')
        file.close()
        toolMantenerTamanyoLog(fichero)

    if TIPO != 'LOG':
        import os
        from datetime import datetime, timedelta

        identificador = TEXT[TEXT.find(' |') + 3:TEXT.find('.')]
        logMail = ROOT + 'Station/scripts/logs/MAIL-Station.log'
        # Define los subject en función del tipo de error
        if TIPO == 'ERROR':
            subject = 'Error en ' + STATION
        elif TIPO == 'SAI':
            subject = 'Problemas con el SAI en ' + STATION
        elif TIPO == 'SPE':
            subject = 'Error en el test de velocidad en ' + STATION
        elif TIPO == 'MON':
            subject = 'Monitorización de la ' + STATION
        elif TIPO == 'RECEP':
            subject = 'Error en la recepción de datos de ' + identificador
        elif TIPO == 'POSIC':
            subject = 'Alarma, la boya ' + STATION + ' se ha soltado'
        elif TIPO == 'ITEM':
            subject = 'Alarma, la temperatura en ' + STATION + ' es muy elevada'
        elif TIPO == 'VOLT':
            subject = 'Alarma, el voltaje en ' + STATION + ' es muy bajo'
        else:
            TIPO = 'ERROR'
            subject = 'Tipo desconocido ' + STATION
        ################################################################################################################

        # Busca en el registro de mails el último correo enviado para este instrumento
        ultimo = '2000-01-01 00:00:00'
        if os.path.isfile(logMail):
            file = open(logMail, 'r')
            for line in file:
                if line[:line.find(' |')] == identificador:
                    ultimo = line[line.find(' |') + 3:]
            file.close()

            ultimo = datetime(int(ultimo[0:4]), int(ultimo[5:7]), int(ultimo[8:10]), int(ultimo[11:13]),
                              int(ultimo[14:16]), int(ultimo[17:19]))
            # print('   ULTIMO='+str(ultimo))
            ahora = datetime.now()
            hacemas = ahora - timedelta(hours=horas)
            # print('   HACE3='+str(hace3))
            if ultimo < hacemas:
                sendmail = 'Y'
                # print ('El último mail enviado es de hace más de 24h, se enviará un correo a '+DEST)
            else:
                sendmail = 'N'
                # print ('El último mail enviado es de hace menos de 3h')
                # print ('No es necesario enviar mail')
        else:
            sendmail = 'Y'

        # Envia el correo en caso de ser necesario
        if sendmail == 'Y':
            linea_log = identificador + ' | ' + toolInstant('%Y-%m-%d %H:%M:%S') + ' -  Notificado a: ' + DEST
            toolSendMail(FROM, PASS, DEST, subject, TEXT)
            file = open(logMail, 'a+')
            file.write(linea_log + '\n')
            file.close()
            toolMantenerTamanyoLog(logMail)

    #     #Define el identificador para el registro de MAIL
    #     if (STATION != 'DataReception'):
    #         IDENTIFICADOR = TIPO
    #     else:
    #         X             = TEXT.find('. -')
    #         IDENTIFICADOR = TEXT[X+3:]
    #         X             = IDENTIFICADOR.find('- ')
    #         IDENTIFICADOR = IDENTIFICADOR[:X]


###############################################################################
#
#
# 66-toolMantenerTamanyoLog: FUNCION PARA MANTENER EL TAMAÑO DEL LOG EN 5000 LINEAS COMO MÁXIMO #####
def toolMantenerTamanyoLog(FICHERO):
    from os import system, path
    if path.isfile(FICHERO):
        FICHERO_TMP = FICHERO[0:FICHERO.find('.')] + 'TMP'
        COMMAND = 'tail -5000' + ' ' + FICHERO + ' > ' + FICHERO_TMP
        system(COMMAND)
        COMMAND = 'rm ' + FICHERO
        system(COMMAND)
        COMMAND = 'mv ' + FICHERO_TMP + ' ' + FICHERO
        system(COMMAND)


###############################################################################
#
#
# 67-encuentraFichero####
def toolEncuentraFichero(DIRLOCAL, EST_NAME, DATAFOLDER, CADA, FROM, PASS, TO):
    import os
    import pathlib
    from datetime import datetime, timedelta

    FILESINFOLDER = [arch.name for arch in sorted(pathlib.Path(DATAFOLDER).iterdir(), key=os.path.getmtime) if
                     arch.is_file()]
    if (not FILESINFOLDER):
        TEXT = '-' + EST_NAME + '- No se encuentran ficheros el directorio de recepción de datos.'
        # print (TEXT)
        TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_' + EST_NAME + '. ' + TEXT
        toolAnyadeLog(DIRLOCAL, '', 'ERROR', TEXT, FROM, PASS, TO)
        RESULTADO = 'PROBLEM'
    else:
        ULTFILE = FILESINFOLDER[len(FILESINFOLDER) - 1]
        # print ('      El último fichero recibido es: '+ULTFILE)
        ULTFILE = DATAFOLDER + '/' + ULTFILE
        AHORA = datetime.now()
        MAXDELAY = AHORA - timedelta(minutes=int(CADA))
        # print ('         Ahora = '+str(AHORA))
        # print ('      maxDelay = '+str(MAXDELAY))

        FNAME = pathlib.Path(ULTFILE)
        FTIME = datetime.fromtimestamp(FNAME.stat().st_mtime)
        # print('      fileTime = '+str(FTIME))
        if (MAXDELAY > FTIME):
            TEXT = '-' + EST_NAME + '- El último fichero recibido es demasiado antuguo: Fichero ' + ULTFILE
            # print (TEXT)
            TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | ERROR_' + EST_NAME + '. ' + TEXT
            toolAnyadeLog(DIRLOCAL, '', 'ERROR', TEXT, FROM, PASS, TO)
            RESULTADO = 'PROBLEM'
        else:
            TEXT = '-' + EST_NAME + '- Fichero recibido en el momento esperado.'
            # print (TEXT)
            TEXT = toolInstant('%Y-%m-%d %H:%M:%S') + ' | LOG_' + EST_NAME + '. ' + TEXT
            toolAnyadeLog(DIRLOCAL, '', 'LOG', TEXT, FROM, PASS, TO)
            RESULTADO = ULTFILE
            compruebaAnteriorProblema(DIRLOCAL, EST_NAME, EST_NAME, FROM, PASS, TO)

    return RESULTADO


##########################################################################
#
#
# 68-toolEncuentraFicherosDaily
def toolEncuentraFicherosDaily(EST_NAME, DATAFOLDER):
    import os
    LSFL = []
    # Lista con todos los ficheros del directorio:
    LSDR = os.walk(DATAFOLDER, topdown=True)  # os.walk()Lista directorios y ficheros
    # Crea una lista de los ficheros ail que existen en el directorio y los incluye a la lista.
    for root, dirs, files in LSDR:
        for FILE in sorted(files):
            #           print ('Leyendo el fichero '+FILE)
            (FILE_NAME, EXT) = os.path.splitext(FILE)
            if (EXT == '.ail'):
                if (FILE_NAME[0:len('RT_Day')] == 'RT_Day'):
                    LSFL.append(FILE_NAME + EXT)
        N_FILES_Day = len(LSFL)
    LSDR = os.walk(DATAFOLDER, topdown=True)  # os.walk()Lista directorios y ficheros
    for root, dirs, files in LSDR:
        for FILE in sorted(files):
            #           print ('Leyendo el fichero '+FILE)
            (FILE_NAME, EXT) = os.path.splitext(FILE)
            if (EXT == '.ail'):
                if (FILE_NAME[0:len('RT_10min')] == 'RT_10min'):
                    LSFL.append(FILE_NAME + EXT)
        N_FILES_10min = len(LSFL)

        N_FILES = N_FILES_Day + N_FILES_10min
        print("Se han encomntrado ", N_FILES, " ficheros en el directorio " + DATAFOLDER)
    return LSFL


###############################################################################
#
#
# 69-toolEncuentraEncuentraEXT
def toolEncuentraEXT(DATADIR, EXT):
    import os
    LSFL = []
    LSDR = os.walk(DATADIR, topdown=True)  # os.walk()Lista directorios y ficheros
    for root, dirs, files in sorted(LSDR):
        for FILE in files:
            (FILE_NAME, EXTEN) = os.path.splitext(FILE)
            if (EXTEN == EXT):
                LSFL.append(FILE_NAME + EXT)
    return LSFL


###############################################################################
#
#
#
def toolPreparaDir(DIR, ):
    ROOT, FOLDER_1, FOLDER_2, FILENAME = toolSepara2Level(DIR)
    toolCompruebaFolder(ROOT + FOLDER_1)
    toolCompruebaFolder(ROOT + FOLDER_1 + '/' + FOLDER_2)


###############################################################################
#
#
#
def toolSepara1LevelNF(DIR, ):
    barra_1 = DIR.rindex('/')
    folder_1 = DIR[barra_1 + 1:]
    root = DIR[:barra_1 + 1]

    return root, folder_1


###############################################################################


def toolSepara2LevelNF(DIR, ):
    barra_1 = DIR.rindex('/')
    folder_1 = DIR[barra_1 + 1:]

    resto_1 = DIR[:barra_1]
    barra_2 = resto_1.rindex('/')
    folder_2 = DIR[barra_2 + 1:barra_1]

    root = DIR[:barra_2 + 1]

    return root, folder_1, folder_2


###############################################################################


def toolSepara2Level(DIR, ):
    BARRA_1 = DIR.rindex('/')
    FILENAME = DIR[BARRA_1 + 1:]

    RESTO_1 = DIR[:BARRA_1]
    BARRA_2 = RESTO_1.rindex('/')
    FOLDER_2 = DIR[BARRA_2 + 1:BARRA_1]

    RESTO_2 = DIR[:BARRA_2]
    BARRA_3 = RESTO_2.rindex('/')

    FOLDER_1 = DIR[BARRA_3 + 1:BARRA_2]

    ROOT = DIR[:BARRA_3 + 1]
    return ROOT, FOLDER_1, FOLDER_2, FILENAME


###############################################################################
#
#
#
# 70-toolConpruebaFolder Comprueba si existe una carpeta y si no existe, la crea
def toolCompruebaFolder(DIR, ):
    import os
    try:
        os.stat(DIR)
    except:
        os.mkdir(DIR)


###############################################################################
#
#
#
# PROGRAMADOR DE TAREAS
#
########################################################################################################################
########################################################################################################################

#
# 81-PROGRAMADOR DE TAREAS######################################################
def programador(TAREA, FileINPUT, PARAM_1, PARAM_2, PARAM_3, PARAM_4, ROOT, STATION, MailFROM, MailPASS, MailDEST):
    import sched
    #    import datetime
    from time import time, sleep
    interval = float(PARAM_1)
    # ahora = datetime.datetime.now()
    INI = prog_Calcula_INI(interval)
    PROG_INICIO = sched.scheduler(time, sleep)
    PROG_INICIO.enterabs(INI, 1, prog_TareaLanza, (
        TAREA, FileINPUT, PARAM_1, PARAM_2, PARAM_3, PARAM_4, ROOT, STATION, MailFROM, MailPASS, MailDEST))
    PROG_INICIO.run()


###############################################################################
#
#
# 82-CALCULA EL INICIO DE UNA TAREA######################################
def prog_Calcula_INI(INTERVAL):
    import datetime
    NOW = datetime.datetime.now()
    if (INTERVAL <= 60):
        # print ('Opcion <= 60')
        SIG = datetime.timedelta(minutes=1)
        INI = NOW + SIG
        INI = datetime.datetime(INI.year, INI.month, INI.day, INI.hour, INI.minute, 0)
    elif (60 < INTERVAL <= 600):
        # print ('60 < Opcion <= 600')
        # print ('NOW='+str(NOW.minute))
        from math import ceil
        MIN = ceil((NOW.minute / 6) * 6 / 10) * 10
        # print ('MIN='+str(MIN))
        if (MIN <= 60):
            INI = datetime.datetime(NOW.year, NOW.month, NOW.day, NOW.hour, MIN, 0)
        else:
            SIG = datetime.timedelta(hours=1)
            INI = NOW + SIG
            INI = datetime.datetime(INI.year, INI.month, INI.day, INI.hour, 0, 0)
    elif (INTERVAL > 600):
        print('Opcion > 600')
        SIG = datetime.timedelta(hours=1)
        INI = NOW + SIG
        INI = datetime.datetime(INI.year, INI.month, INI.day, INI.hour, 0, 0)

    # print ('La tarea se lanzara a las:', str(INI))
    INI = INI.timestamp()
    print()
    return (INI)


########################################################################
#
#
# 83-FUNCION QUE LANZA LA TAREA##########################################
def prog_TareaLanza(TAREA, FileINPUT, PARAM_1, PARAM_2, PARAM_3, PARAM_4, ROOT, STATION, MailFROM, MailPASS, MailDEST):
    import sched
    #    import datetime
    from time import time, sleep
    INTERVAL = float(PARAM_1)
    # print (toolInstant('%Y-%m-%d %H:%M:%S')+' - TAREA_LANZA')
    PROG_REPITE = sched.scheduler(time, sleep)
    PROG_REPITE.enter(0, 1, prog_TareaEjecuta, (
        TAREA, FileINPUT, PARAM_1, PARAM_2, PARAM_3, PARAM_4, ROOT, STATION, MailFROM, MailPASS, MailDEST))
    PROG_REPITE.run()
    while True:
        PROG_REPITE.enter(INTERVAL, 1, prog_TareaEjecuta, (
            TAREA, FileINPUT, PARAM_1, PARAM_2, PARAM_3, PARAM_4, ROOT, STATION, MailFROM, MailPASS, MailDEST))
        PROG_REPITE.run()


########################################################################
#
#
# 84-FUNCION QUE EJECUTA LA TAREA########################################
def prog_TareaEjecuta(TAREA, FileINPUT, PARAM_1, PARAM_2, PARAM_3, PARAM_4, ROOT, STATION, MailFROM, MailPASS,
                      MailDEST):
    # print (toolInstant('%Y-%m-%d %H:%M:%S')+' - TAREA_EJECUTA '+ TAREA)
    # print ('Tarea= '+str(TAREA))
    from threading import Thread
    subproceso = Thread(target=eval(TAREA),
                        args=(FileINPUT, PARAM_2, PARAM_3, PARAM_4, ROOT, STATION, MailFROM, MailPASS, MailDEST))
    subproceso.start()


########################################################################
#
#
#
# BANNER
#
########################################################################################################################
########################################################################################################################
#
# 91-lanzaBanner: FUNCION LIMPIAR LA PANTALLA Y PRESENTAR UN BANNER #####
def lanzaBanner_IME(VER):
    from os import system
    system('clear')
    print(' ')
    print('  Inicio de la comprobación de recepcion de datos')
    print(' ')
    print('      ___  __  __  _____  ____   _____     _     ')
    print('     |_ _||  \/  || ____||  _ \ | ____|   / \    ')
    print('      | | | |\/| ||  _|  | | | ||  _|    / _ \   ')
    print('      | | | |  | || |___ | |_| || |___  / ___ \  ')
    print('     |___||_|  |_||_____||____/ |_____|/_/   \_\ ')
    print(' ')
    print('   -scriptVersion: ' + VER + '-')


########################################################################
#
#
# 92-lanzaBanner: FUNCION LIMPIAR LA PANTALLA Y PRESENTAR UN BANNER #####
def lanzaBanner_SCB(VER):
    from os import system
    system('clear')
    print(' ')
    print('  Inicio de la comprobación de recepcion de datos')
    print(' ')
    print('         S)ssss   O)oooo    C)ccc  I)iiii B)bbbb')
    print('        S)    ss O)    oo  C)   cc   I)   B)   bb')
    print('         S)ss    O)    oo C)         I)   B)bbbb')
    print('             S)  O)    oo C)         I)   B)   bb')
    print('        S)    ss O)    oo  C)   cc   I)   B)    bb')
    print('         S)ssss   O)oooo    C)ccc  I)iiii B)bbbbb')
    print(' ')
    print('   -scriptVersion: ' + VER + '-')


########################################################################
#
#
# FIGURAS
########################################################################################################################
########################################################################################################################
#
#
#
# 101-GRAFICO DE DOS SERIES #####
def plot_2X2serie(TIMELINE, VAR_0, VAR_1, ID_VAR_0, ID_VAR_1, TITLE, YLAB_0, YLAB_1, DIAS, OUTFILE):
    import datetime
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib.offsetbox import AnchoredText
    fig, ax = plt.subplots(2, figsize=(10, 5))
    fig.suptitle(TITLE)
    ax[0].plot(TIMELINE, VAR_0, 'r')
    ax[1].plot(TIMELINE, VAR_1, 'g')

    hours = mdates.HourLocator(interval=24)  #
    date_form = mdates.DateFormatter('%d/%m')
    ax[0].xaxis.set_major_locator(hours)
    ax[0].xaxis.set_major_formatter(date_form)
    ax[1].xaxis.set_major_locator(hours)
    ax[1].xaxis.set_major_formatter(date_form)

    MAXX = datetime.date.today() + datetime.timedelta(days=1)
    MINX = datetime.date.today() - datetime.timedelta(days=DIAS)

    MINY_0 = min(VAR_0) - 0.3
    MAXY_0 = max(VAR_0) + 0.3
    MINY_1 = min(VAR_1) - 0.3
    MAXY_1 = max(VAR_1) + 0.3
    ax[0].set(xlim=[MINX, MAXX])
    ax[1].set(xlim=[MINX, MAXX])
    ax[0].set(ylim=[MINY_0, MAXY_0])
    ax[1].set(ylim=[MINY_1, MAXY_1])

    ax[1].set(xlabel=datetime.datetime.now().year)
    ax[0].set(ylabel=YLAB_0)
    ax[1].set(ylabel=YLAB_1)

    ax[0].grid(True)
    ax[1].grid(True)

    # Pinta una caja con la fecha del ultimo mensaje y la variable
    text = AnchoredText(str(TIMELINE[len(TIMELINE) - 1]) + '; ' + YLAB_0[0:YLAB_0.find('(') - 1] + '=' + str(
        VAR_0[len(VAR_0) - 1]) + YLAB_0[YLAB_0.find('(') + 1:YLAB_0.find(')')], loc=3, prop={'size': 10}, frameon=True)
    ax[0].add_artist(text)
    text = AnchoredText(str(TIMELINE[len(TIMELINE) - 1]) + '; ' + YLAB_1[0:YLAB_1.find('(') - 1] + '=' + str(
        VAR_1[len(VAR_1) - 1]) + YLAB_1[YLAB_1.find('(') + 1:YLAB_1.find(')')], loc=3, prop={'size': 10}, frameon=True)
    ax[1].add_artist(text)

    # Pinta una caja con los máximos y mínimos
    text = AnchoredText('Máximo= ' + str(max(VAR_0)) + YLAB_0[YLAB_0.find('(') + 1:YLAB_0.find(')')] + '; Mínimo' + str(
        min(VAR_0)) + YLAB_0[YLAB_0.find('(') + 1:YLAB_0.find(')')], loc=4, prop={'size': 10}, frameon=True)
    ax[0].add_artist(text)
    text = AnchoredText('Máximo= ' + str(max(VAR_1)) + YLAB_1[YLAB_1.find('(') + 1:YLAB_1.find(')')] + '; Mínimo' + str(
        min(VAR_1)) + YLAB_1[YLAB_1.find('(') + 1:YLAB_1.find(')')], loc=4, prop={'size': 10}, frameon=True)
    ax[1].add_artist(text)

    plt.savefig(OUTFILE, bbox_inches='tight')


#    plt.show()
########################################################################
# %%
#
# 102-FIGURA DE LA POSICION DE UNA BOYA #####
def plot_Posicion(DATE, LAT_REF, LON_REF, RADI_UMB, LAT, LON, DIST, OUTFILE):
    import matplotlib.pyplot as plt
    import numpy as np
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    from matplotlib.offsetbox import AnchoredText
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
    from colour import Color
    # pip install colour

    LAT_REF = float(LAT_REF)
    LON_REF = float(LON_REF)
    RADI_UMB = float(RADI_UMB)
    LAT = tuple(float(i) for i in LAT)
    LON = tuple(float(i) for i in LON)
    if (RADI_UMB > float(DIST[len(DIST) - 1])):
        RG = RADI_UMB * 1.3 / 100000
    else:
        RG = float(DIST[len(DIST) - 1]) * 1.3 / 100000

    fig = plt.figure(figsize=(15, 10))
    # ax  = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())

    # Añade la textura del océano
    ax.add_feature(cfeature.OCEAN)
    #    ax.add_feature(cfeature.COASTLINE)
    #    bathym = cfeature.NaturalEarthFeature(name='bathymetry_J_1000', scale='10m', category='physical')
    #    ax.add_feature(bathym, edgecolor='gray')

    # Ticks
    ax.set_xticks(np.arange(LON_REF - RG, LON_REF + RG, RG), crs=ccrs.PlateCarree())
    ax.set_yticks(np.arange(LAT_REF - RG, LAT_REF + RG, RG), crs=ccrs.PlateCarree())
    ax.xaxis.set_major_formatter(LongitudeFormatter())
    ax.yaxis.set_major_formatter(LatitudeFormatter())

    # Fija el tamaño de los ejes
    ax.set_extent([LON_REF - RG, LON_REF + RG, LAT_REF - RG, LAT_REF + RG], crs=ccrs.PlateCarree())

    # Pinta un círculo de radio X
    ax.tissot(rad_km=RADI_UMB / 1000, lons=LON_REF, lats=LAT_REF, alpha=0.3)

    # Pinta lineas eje
    geodetic = ccrs.Geodetic()
    robinson = ccrs.Robinson()

    IN_lat, IN_lon = LAT_REF, LON_REF - RG
    EN_lat, EN_lon = LAT_REF, LON_REF + RG

    IN_lon_t, IN_lat_t = robinson.transform_point(IN_lon, IN_lat, geodetic)
    EN_lon_t, EN_lat_t = robinson.transform_point(EN_lon, EN_lat, geodetic)

    plt.plot([IN_lon_t, EN_lon_t], [IN_lat_t, EN_lat_t],
             color='grey', linewidth=1,
             # Be explicit about which transform you want:
             transform=robinson)

    IN_lat, IN_lon = LAT_REF - RG, LON_REF
    EN_lat, EN_lon = LAT_REF + RG, LON_REF

    IN_lon_t, IN_lat_t = robinson.transform_point(IN_lon, IN_lat, geodetic)
    EN_lon_t, EN_lat_t = robinson.transform_point(EN_lon, EN_lat, geodetic)

    plt.plot([IN_lon_t, EN_lon_t], [IN_lat_t, EN_lat_t],
             color='grey', linewidth=1,
             # Be explicit about which transform you want:
             transform=robinson)

    # Pinta el centro en azul
    ax.plot(LON_REF, LAT_REF, 'bo', markersize=7, transform=ccrs.Geodetic())

    # Pinta las posiciones de las ultimas horas
    GRIS = Color("grey")
    colors = list(GRIS.range_to("yellow", len(LAT)))
    for n in range(len(LAT)):
        # ax.text(float(LON[n]), float(LAT[n]), '·', transform=ccrs.Geodetic())
        ax.plot(LON[n], LAT[n], color=str(colors[n]), marker='o', markersize=4, transform=ccrs.Geodetic())
        # Pinta la última posición en rojo
    ax.plot(LON[n], LAT[n], 'ro', markersize=7, markeredgewidth=1.3, markeredgecolor='blue', transform=ccrs.Geodetic())

    # Pinta una caja con la fecha del ultimo mensaje y la distancia
    text = AnchoredText('{}; Distancia: {}'
                        ''.format(str(DATE[len(DATE) - 1]), str(DIST[len(DIST) - 1]) + 'm'),
                        loc=4, prop={'size': 12}, frameon=True)
    ax.add_artist(text)
    # Pinta una caja con el radio umbral
    text = AnchoredText('Umbral: {}'
                        ''.format(str(RADI_UMB) + 'm'),
                        loc=1, prop={'size': 12}, frameon=True)
    ax.add_artist(text)

    # Pinta una línea entre el centro y la última posición recibida
    IN_lat, IN_lon = float(LAT_REF), float(LON_REF)
    EN_lat, EN_lon = float(LAT[len(LAT) - 1]), float(LON[len(LON) - 1])

    IN_lon_t, IN_lat_t = robinson.transform_point(IN_lon, IN_lat, geodetic)
    EN_lon_t, EN_lat_t = robinson.transform_point(EN_lon, EN_lat, geodetic)

    plt.plot([IN_lon_t, EN_lon_t], [IN_lat_t, EN_lat_t],
             color='blue', linewidth=1,
             # Be explicit about which transform you want:
             transform=robinson)

    plt.savefig(OUTFILE, bbox_inches='tight')


#    plt.show()
########################################################################


def buscaFicheros(DIR, CONDI_I, CONDI_E):
    import os
    LSFL = []
    # Lista con todos los ficheros del directorio:
    LSDR = os.walk(DIR, topdown=True)  # os.walk()Lista directorios y ficheros
    # Crea una lista de los ficheros ail que existen en el directorio y los incluye a la lista.
    for root, dirs, files in LSDR:
        for FILE in sorted(files):
            #           print ('Leyendo el fichero '+FILE)
            (FILE_NAME, EXT) = os.path.splitext(FILE)
            if (EXT == CONDI_E):
                if (FILE_NAME[0:len(CONDI_I)] == CONDI_I):
                    LSFL.append(FILE_NAME + EXT)
        N_FILES = len(LSFL)
        print("Se han encomntrado ", N_FILES, " ficheros en el directorio " + DIR)
    return LSFL


# XX-leeDataOlas: Funcion para leer los datos de oleaje de la Boya de Soller
def leeDataOlas(DIR, CONDI_I, CONDI_E):
    import csv
    from datetime import datetime
    TMLN = []
    WHEI = []
    WMAX = []
    WDIR = []
    WPER = []
    LSFL = buscaFicheros(DIR, CONDI_I, CONDI_E)

    for N in range(len(LSFL)):
        FILE = DIR + '/' + LSFL[N]
        print('Leyendo los datos del fichero ' + LSFL[N])
        with open(FILE, newline='') as csvfile:
            DATA = csv.reader(csvfile, delimiter=',')
            CONT = 1
            for ROW in DATA:
                if (CONT > 4):
                    TMLN.append(datetime.strptime(ROW[0], '%Y-%m-%d %H:%M:%S'))
                    WHEI.append(float(ROW[2]))
                    WMAX.append(float(ROW[3]))
                    WPER.append(float(ROW[4]))
                    WDIR.append(float(ROW[5]))
                CONT = CONT + 1

    return TMLN, WHEI, WMAX, WPER, WDIR


######################################################################
# %%
#
# XX-leeDataMeteo: Funcion para leer los datos meteorologicos de la Boya de Soller
def leeDataMeteo(DIR, CONDI_I, CONDI_E):
    import csv
    from datetime import datetime

    LSFL = buscaFicheros(DIR, CONDI_I, CONDI_E)
    TMLN = []
    APRE = []
    ATEM = []
    WSPE = []
    WGUS = []
    WWDR = []
    # Lee los datos
    for N in range(len(LSFL)):
        FILE = DIR + '/' + LSFL[N]
        with open(FILE, newline='') as csvfile:
            DATA = csv.reader(csvfile, delimiter=',')
            CONT = 1
            for ROW in DATA:
                if (CONT > 4):
                    TMLN.append(datetime.strptime(ROW[0], '%Y-%m-%d %H:%M:%S'))
                    APRE.append(float(ROW[2]) * 1000)
                    ATEM.append(float(ROW[3]))
                    WSPE.append(float(ROW[4]))
                    WGUS.append(float(ROW[5]))
                    WWDR.append(float(ROW[7]))
                CONT = CONT + 1

    return TMLN, APRE, ATEM, WSPE, WGUS, WWDR


######################################################################
# %%
#
# XX-leeDataStatus: Funcion para leer los datos de estado de la Boya de Soller
def leeDataStatus(DIR, CONDI_I, CONDI_E):
    import csv
    from datetime import datetime

    LSFL = buscaFicheros(DIR, CONDI_I, CONDI_E)
    TMLN = []
    LATI = []
    LONG = []
    NSAT = []
    PITC = []
    ROLL = []
    TEMP = []
    BVOL = []

    # Lee los datos
    for N in range(len(LSFL)):
        FILE = DIR + '/' + LSFL[N]
        with open(FILE, newline='') as csvfile:
            DATA = csv.reader(csvfile, delimiter=',')
            CONT = 1
            for ROW in DATA:
                if (CONT > 4):
                    TMLN.append(datetime.strptime(ROW[0], '%Y-%m-%d %H:%M:%S'))
                    LAT = (ROW[6])
                    LATI.append(float(LAT[0:2]) + (float(LAT[2:]) / 60))
                    LON = (ROW[7])
                    LONG.append(float(LON[0:3]) + (float(LON[3:]) / 60))
                    NSAT.append(float(ROW[8]))
                    PITC.append(float(ROW[9]))
                    ROLL.append(float(ROW[10]))
                    TEMP.append(float(ROW[12]))
                    BVOL.append(float(ROW[13]))

                CONT = CONT + 1

    return TMLN, LATI, LONG, NSAT, PITC, ROLL, TEMP, BVOL


######################################################################


# 101-GRAFICO DE DOS SERIES #####
def plotStation_2Var(timeline, var_1, var_2, label_1, label_2, color_1, color_2, title, outfile):
    import datetime
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib.offsetbox import AnchoredText
    fig, ax = plt.subplots(2, figsize=(12, 6))
    ax[0].plot(timeline, var_1, color_1)
    ax[1].plot(timeline, var_2, color_2)

    hours = mdates.HourLocator(interval=3)  #
    date_form = mdates.DateFormatter('%H:00')
    ax[0].xaxis.set_major_locator(hours)
    ax[0].xaxis.set_major_formatter(date_form)
    ax[1].xaxis.set_major_locator(hours)
    ax[1].xaxis.set_major_formatter(date_form)

    maxx = datetime.date.today() + datetime.timedelta(days=1)
    minx = datetime.date.today() - datetime.timedelta(days=0)

    miny_1 = min(var_1) - 0.3
    maxy_1 = max(var_1) + 0.3
    miny_2 = min(var_2) - 0.3
    maxy_2 = max(var_2) + 0.3
    ax[0].set(xlim=[minx, maxx])
    ax[1].set(xlim=[minx, maxx])
    ax[0].set(ylim=[miny_1, maxy_1])
    ax[1].set(ylim=[miny_2, maxy_2])

    ax[1].set(xlabel=datetime.datetime.now().strftime("%Y-%m-%d"))
    ax[0].set(ylabel=label_1)
    ax[1].set(ylabel=label_2)

    ax[0].grid(True)
    ax[1].grid(True)

    # Pinta una caja con la fecha del ultimo mensaje y la variable
    text = AnchoredText(str(timeline[len(timeline) - 1]) + '; ' + label_1[0:label_1.find('(') - 1] + '=' + str(
        var_1[len(var_1) - 1]) + label_1[label_1.find('(') + 1:label_1.find(')')], loc=3, prop={'size': 10},
                        frameon=True)
    ax[0].add_artist(text)
    text = AnchoredText(str(timeline[len(timeline) - 1]) + '; ' + label_2[0:label_2.find('(') - 1] + '=' + str(
        var_2[len(var_2) - 1]) + label_2[label_2.find('(') + 1:label_2.find(')')], loc=3, prop={'size': 10},
                        frameon=True)
    ax[1].add_artist(text)

    # Pinta una caja con los máximos y mínimos
    text = AnchoredText(
        'Máximo= ' + str(max(var_1)) + label_1[label_1.find('(') + 1:label_1.find(')')] + '; Mínimo' + str(
            min(var_1)) + label_1[label_1.find('(') + 1:label_1.find(')')], loc=4, prop={'size': 10}, frameon=True)
    ax[0].add_artist(text)
    text = AnchoredText(
        'Máximo= ' + str(max(var_2)) + label_2[label_2.find('(') + 1:label_2.find(')')] + '; Mínimo' + str(
            min(var_2)) + label_2[label_2.find('(') + 1:label_2.find(')')], loc=4, prop={'size': 10}, frameon=True)
    ax[1].add_artist(text)

    plt.savefig(outfile, bbox_inches='tight')
    # plt.show()


########################################################################

def plotStation_1Var(timeline, var_1, label_1, color_1, title, outfile):
    import datetime
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib.offsetbox import AnchoredText
    fig, ax = plt.subplots(1, figsize=(12, 3))
    ax.plot(timeline, var_1, color_1)

    hours = mdates.HourLocator(interval=3)  #
    date_form = mdates.DateFormatter('%H:00')
    ax.xaxis.set_major_locator(hours)
    ax.xaxis.set_major_formatter(date_form)

    maxx = datetime.date.today() + datetime.timedelta(days=1)
    minx = datetime.date.today() - datetime.timedelta(days=0)

    miny_1 = min(var_1) - 0.3
    maxy_1 = max(var_1) + 0.3
    ax.set(xlim=[minx, maxx])
    ax.set(ylim=[miny_1, maxy_1])

    ax.set(xlabel=datetime.datetime.now().strftime("%Y-%m-%d"))
    ax.set(ylabel=label_1)

    ax.grid(True)

    # Pinta una caja con la fecha del ultimo mensaje y la variable
    text = AnchoredText(str(timeline[len(timeline) - 1]) + '; ' + label_1[0:label_1.find('(') - 1] + '=' + str(
        var_1[len(var_1) - 1]) + label_1[label_1.find('(') + 1:label_1.find(')')], loc=3, prop={'size': 10},
                        frameon=True)
    ax.add_artist(text)

    # Pinta una caja con los máximos y mínimos
    text = AnchoredText(
        'Máximo= ' + str(max(var_1)) + label_1[label_1.find('(') + 1:label_1.find(')')] + '; Mínimo' + str(
            min(var_1)) + label_1[label_1.find('(') + 1:label_1.find(')')], loc=4, prop={'size': 10}, frameon=True)
    ax.add_artist(text)

    plt.savefig(outfile, bbox_inches='tight')
    # plt.show()


########################################################################


# LECTURA DE DATOS
#######################################################################################################################

def leeTempHum(FILE):
    import numpy as np
    from datetime import datetime

    # Prepara variables
    LIST_FILES = []
    TIMELINE = []
    TEMPERATURA = []
    HUMEDAD = []

    # Lee los datos
    DATOS = np.genfromtxt(FILE, dtype=bytes).astype(str)
    for i in range(len(DATOS)):
        TIMELINE.append(datetime.strptime(DATOS[i, 0] + ' ' + DATOS[i, 1], '%Y-%m-%d %H:%M:%S'))
        TEMPERATURA.append(float(DATOS[i, 3][5:9]))
        HUMEDAD.append(float(DATOS[i, 4][4:8]))

    return TIMELINE, TEMPERATURA, HUMEDAD


def leeTemp(file):
    import numpy as np
    from datetime import datetime

    # Prepara variables
    timeline = []
    temperatura = []

    # Lee los datos
    datos = np.genfromtxt(file, dtype=bytes).astype(str)
    for i in range(len(datos)):
        timeline.append(datetime.strptime(datos[i, 0] + ' ' + datos[i, 1], '%Y-%m-%d %H:%M:%S'))
        temperatura.append(float(datos[i, 3][5:9]))

    return timeline, temperatura
