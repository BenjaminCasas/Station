#
#
# 7-leeDataAQP: FUNCION DE LECTURA DE LOS DATOS .dat y .sen DE UN CORRENTIMETRO AQUADOPP#########################
def leeDataAQP(DATADIR):
    import datetime
    import numpy as np
    DIST = []
    # Busca la información eb en el fichero .hdr
    LIST_FILES = toolEncuentraEXT(DATADIR, '.hdr')
    for i in range(len(LIST_FILES)):
        FICHERO = open('DATOS/' + LIST_FILES[i], 'r')
        print('Leyentdo el fichero ' + LIST_FILES[i])
        DATOS = FICHERO.readlines()
        N_CELLS = DATOS[10]
        N_CELLS = int(N_CELLS[N_CELLS.rfind(' ', 30, N_CELLS.find('\n')) + 1:N_CELLS.find('\n')])

        for n in range(N_CELLS):
            LINE = DATOS[144 + n]
            DIST.append(float(LINE.split()[1]))

        FICHERO.close()
        del DATOS, LINE

    # Carga los datos del fichero .dat
    LIST_FILES = toolEncuentraEXT(DATADIR, '.dat')
    TIMELINE = []
    ERROR_CD = []
    STATUS_CD = []
    BATT_VOL = []
    SOUND_SP = []
    HEADING = []
    PITCH = []
    ROLL = []
    PRESS = []
    WTEMP = []
    V_EAST = []
    V_NORTH = []
    V_UP = []
    AMP_B1 = []
    AMP_B2 = []
    AMP_B3 = []
    V_SPEE = []
    V_DIR = []
    for i in range(len(LIST_FILES)):
        FICHERO = open('DATOS/' + LIST_FILES[i], 'r')
        print('Leyentdo el fichero ' + LIST_FILES[i])
        DATOS = FICHERO.readlines()

        for n in range(int(float(len(DATOS)) / (N_CELLS + 1))):
            TIMELINE.append(
                datetime.datetime(int(DATOS[(N_CELLS + 1) * n].split()[2]), int(DATOS[(N_CELLS + 1) * n].split()[0]),
                                  int(DATOS[(N_CELLS + 1) * n].split()[1]), int(DATOS[(N_CELLS + 1) * n].split()[3]),
                                  int(DATOS[(N_CELLS + 1) * n].split()[4]), int(DATOS[(N_CELLS + 1) * n].split()[5])))
            ERROR_CD.append(float(DATOS[(N_CELLS + 1) * n].split()[6]))
            STATUS_CD.append(float(DATOS[(N_CELLS + 1) * n].split()[7]))
            BATT_VOL.append(float(DATOS[(N_CELLS + 1) * n].split()[8]))
            SOUND_SP.append(float(DATOS[(N_CELLS + 1) * n].split()[9]))
            HEADING.append(float(DATOS[(N_CELLS + 1) * n].split()[10]))
            PITCH.append(float(DATOS[(N_CELLS + 1) * n].split()[11]))
            ROLL.append(float(DATOS[(N_CELLS + 1) * n].split()[12]))
            PRESS.append(float(DATOS[(N_CELLS + 1) * n].split()[13]))
            WTEMP.append(float(DATOS[(N_CELLS + 1) * n].split()[14]))

            V_EAST.append([])
            V_NORTH.append([])
            V_UP.append([])
            AMP_B1.append([])
            AMP_B2.append([])
            AMP_B3.append([])
            V_SPEE.append([])
            V_DIR.append([])
            for m in range(N_CELLS):
                V_EAST[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[2]))
                V_NORTH[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[3]))
                V_UP[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[4]))
                AMP_B1[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[5]))
                AMP_B2[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[6]))
                AMP_B3[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[7]))
                V_SPEE[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[8]))
                V_DIR[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[9]))

        FICHERO.close()
        del DATOS

        V_EAST = np.array(V_EAST)
        V_NORTH = np.array(V_NORTH)
        V_UP = np.array(V_UP)
        AMP_B1 = np.array(AMP_B1)
        AMP_B2 = np.array(AMP_B2)
        AMP_B3 = np.array(AMP_B3)
        V_SPEE = np.array(V_SPEE)
        V_DIR = np.array(V_DIR)

    return TIMELINE, N_CELLS, DIST, ERROR_CD, STATUS_CD, BATT_VOL, SOUND_SP, HEADING, PITCH, ROLL, PRESS, WTEMP, V_EAST, V_NORTH, V_UP, AMP_B1, AMP_B2, AMP_B3, V_SPEE, V_DIR


########################################################################################################################
#
#
# 8-leeDataAQP_HR: FUNCION DE LECTURA DE LOS DATOS .dat y .sen DE UN CORRENTIMETRO AQUADOPP#########################
def leeDataAQP_HR(DATADIR):
    import datetime
    import numpy as np
    DIST = []
    # Busca la información eb en el fichero .hdr
    LIST_FILES = toolEncuentraEXT(DATADIR, '.hdr')
    for i in range(len(LIST_FILES)):
        FICHERO = open(DATADIR + '/' + LIST_FILES[i], 'r')
        print('Leyentdo el fichero ' + LIST_FILES[i])
        DATOS = FICHERO.readlines()
        N_CELLS = DATOS[19]
        N_CELLS = int(N_CELLS[N_CELLS.rfind(' ', 30, N_CELLS.find('\n')) + 1:N_CELLS.find('\n')])

        for n in range(N_CELLS):
            LINE = DATOS[137 + n]
            DIST.append(float(LINE.split()[1]))

        FICHERO.close()
        del DATOS, LINE

    # Carga los datos del fichero .dat
    LIST_FILES = toolEncuentraEXT(DATADIR, '.dat')
    TIMELINE = []
    ERROR_CD = []
    STATUS_CD = []
    BATT_VOL = []
    SOUND_SP = []
    HEADING = []
    PITCH = []
    ROLL = []
    PRESS = []
    WTEMP = []
    V_EAST = []
    V_NORTH = []
    V_UP = []
    AMP_B1 = []
    AMP_B2 = []
    AMP_B3 = []
    V_SPEE = []
    V_DIR = []
    for i in range(len(LIST_FILES)):
        FICHERO = open(DATADIR + '/' + LIST_FILES[i], 'r')
        print('Leyentdo el fichero ' + LIST_FILES[i])
        DATOS = FICHERO.readlines()

        for n in range(int(float(len(DATOS)) / (N_CELLS + 1))):
            TIMELINE.append(
                datetime.datetime(int(DATOS[(N_CELLS + 1) * n].split()[2]), int(DATOS[(N_CELLS + 1) * n].split()[0]),
                                  int(DATOS[(N_CELLS + 1) * n].split()[1]), int(DATOS[(N_CELLS + 1) * n].split()[3]),
                                  int(DATOS[(N_CELLS + 1) * n].split()[4]), 0))
            ERROR_CD.append(float(DATOS[(N_CELLS + 1) * n].split()[6]))
            STATUS_CD.append(float(DATOS[(N_CELLS + 1) * n].split()[7]))
            BATT_VOL.append(float(DATOS[(N_CELLS + 1) * n].split()[10]))
            SOUND_SP.append(float(DATOS[(N_CELLS + 1) * n].split()[11]))
            HEADING.append(float(DATOS[(N_CELLS + 1) * n].split()[12]))
            PITCH.append(float(DATOS[(N_CELLS + 1) * n].split()[13]))
            ROLL.append(float(DATOS[(N_CELLS + 1) * n].split()[14]))
            PRESS.append(float(DATOS[(N_CELLS + 1) * n].split()[15]))
            WTEMP.append(float(DATOS[(N_CELLS + 1) * n].split()[16]))

            V_EAST.append([])
            V_NORTH.append([])
            V_UP.append([])
            AMP_B1.append([])
            AMP_B2.append([])
            AMP_B3.append([])
            V_SPEE.append([])
            V_DIR.append([])
            for m in range(N_CELLS):
                V_EAST[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[2]))
                V_NORTH[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[3]))
                V_UP[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[4]))
                AMP_B1[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[5]))
                AMP_B2[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[6]))
                AMP_B3[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[7]))
                V_SPEE[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[11]))
                V_DIR[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[12]))

        FICHERO.close()
        del DATOS

        V_EAST = np.array(V_EAST)
        V_NORTH = np.array(V_NORTH)
        V_UP = np.array(V_UP)
        AMP_B1 = np.array(AMP_B1)
        AMP_B2 = np.array(AMP_B2)
        AMP_B3 = np.array(AMP_B3)
        V_SPEE = np.array(V_SPEE)
        V_DIR = np.array(V_DIR)

    return TIMELINE, N_CELLS, DIST, ERROR_CD, STATUS_CD, BATT_VOL, SOUND_SP, HEADING, PITCH, ROLL, PRESS, WTEMP, V_EAST, V_NORTH, V_UP, AMP_B1, AMP_B2, AMP_B3, V_SPEE, V_DIR


########################################################################################################################
#
#
# 9-leeDataVector: FUNCION DE LECTURA DE LOS DATOS .dat y .sen DE UN CORRENTIMETRO VECTOR#########################
def leeDataVector(DATADIR):
    import datetime
    import numpy as np

    # Busca la información eb en el fichero .hdr
    LIST_FILES = toolEncuentraEXT(DATADIR, '.hdr')
    for i in range(len(LIST_FILES)):
        FICHERO = open(DATADIR + '/' + LIST_FILES[i], 'r')
        print('Leyentdo el fichero ' + LIST_FILES[i])
        DATOS = FICHERO.readlines()
        S_RATE = DATOS[11]
        S_RATE = int(S_RATE[S_RATE.rfind('  '):S_RATE.find('Hz')])
        FICHERO.close()
        del DATOS

    # Carga los datos del fichero .sen
    LIST_FILES = toolEncuentraEXT(DATADIR, '.sen')
    TIMELINE = []
    ERROR_CD = []
    STATUS_CD = []
    BATT_VOL = []
    SOUND_SP = []
    HEADING = []
    PITCH = []
    ROLL = []
    WTEMP = []
    for i in range(len(LIST_FILES)):
        FICHERO = open(DATADIR + '/' + LIST_FILES[i], 'r')
        print('Leyentdo el fichero ' + LIST_FILES[i])
        DATOS = FICHERO.readlines()
        for n in range(len(DATOS)):
            TIMELINE.append(
                datetime.datetime(int(DATOS[n].split()[2]), int(DATOS[n].split()[0]), int(DATOS[n].split()[1]),
                                  int(DATOS[n].split()[3]), int(DATOS[n].split()[4]), int(DATOS[n].split()[5])))
            ERROR_CD.append(float(DATOS[n].split()[6]))
            STATUS_CD.append(float(DATOS[n].split()[7]))
            BATT_VOL.append(float(DATOS[n].split()[8]))
            SOUND_SP.append(float(DATOS[n].split()[9]))
            HEADING.append(float(DATOS[n].split()[10]))
            PITCH.append(float(DATOS[n].split()[11]))
            ROLL.append(float(DATOS[n].split()[12]))
            WTEMP.append(float(DATOS[n].split()[13]))

            FICHERO.close()
        del DATOS

    #### OJO ---- PARA CONTINUO Y 1HZ -----------
    # Carga los datos del fichero .dat
    LIST_FILES = toolEncuentraEXT(DATADIR, '.dat')
    V_EAST = []
    V_NORTH = []
    V_UP = []
    AMP_B1 = []
    AMP_B2 = []
    AMP_B3 = []
    PRESS = []
    for i in range(len(LIST_FILES)):
        FICHERO = open(DATADIR + '/' + LIST_FILES[i], 'r')
        print('Leyentdo el fichero ' + LIST_FILES[i])
        DATOS = FICHERO.readlines()
        for n in range(len(DATOS)):
            V_EAST.append(float(DATOS[n].split()[2]))
            V_NORTH.append(float(DATOS[n].split()[3]))
            V_UP.append(float(DATOS[n].split()[4]))
            AMP_B1.append(float(DATOS[n].split()[5]))
            AMP_B2.append(float(DATOS[n].split()[6]))
            AMP_B3.append(float(DATOS[n].split()[7]))
            PRESS.append(float(DATOS[n].split()[14]))

            FICHERO.close()
        del DATOS

        V_EAST = np.array(V_EAST)
        V_NORTH = np.array(V_NORTH)
        V_UP = np.array(V_UP)
        AMP_B1 = np.array(AMP_B1)
        AMP_B2 = np.array(AMP_B2)
        AMP_B3 = np.array(AMP_B3)

        TIMELINE = TIMELINE[0:len(PRESS)]
        ERROR_CD = ERROR_CD[0:len(PRESS)]
        STATUS_CD = STATUS_CD[0:len(PRESS)]
        BATT_VOL = BATT_VOL[0:len(PRESS)]
        SOUND_SP = SOUND_SP[0:len(PRESS)]
        HEADING = HEADING[0:len(PRESS)]
        PITCH = PITCH[0:len(PRESS)]
        ROLL = ROLL[0:len(PRESS)]

        WTEMP = WTEMP[0:len(PRESS)]
    return TIMELINE, ERROR_CD, STATUS_CD, BATT_VOL, SOUND_SP, HEADING, PITCH, ROLL, WTEMP, PRESS, V_EAST, V_NORTH, V_UP, AMP_B1, AMP_B2, AMP_B3


########################################################################################################################
#
#
# 10-leeDataAWAC: FUNCION DE LECTURA DE LOS DATOS .dat y .sen DE UN CORRENTIMETRO AQUADOPP#########################
def leeDataAWAC(DATADIR):
    import datetime
    import numpy as np
    DIST = []
    # Busca la información eb en el fichero .hdr
    LIST_FILES = toolEncuentraEXT(DATADIR, '.hdr')
    for i in range(len(LIST_FILES)):
        FICHERO = open('DATOS/' + LIST_FILES[i], 'r')
        print('Leyentdo el fichero ' + LIST_FILES[i])
        DATOS = FICHERO.readlines()
        N_CELLS = DATOS[10]
        N_CELLS = int(N_CELLS[N_CELLS.rfind(' ', 30, N_CELLS.find('\n')) + 1:N_CELLS.find('\n')])

        for n in range(N_CELLS):
            LINE = DATOS[144 + n]
            DIST.append(float(LINE.split()[1]))

        FICHERO.close()
        del DATOS, LINE

    # Carga los datos del fichero .dat
    LIST_FILES = toolEncuentraEXT(DATADIR, '.dat')
    TIMELINE = []
    ERROR_CD = []
    STATUS_CD = []
    BATT_VOL = []
    SOUND_SP = []
    HEADING = []
    PITCH = []
    ROLL = []
    PRESS = []
    WTEMP = []
    V_EAST = []
    V_NORTH = []
    V_UP = []
    AMP_B1 = []
    AMP_B2 = []
    AMP_B3 = []
    V_SPEE = []
    V_DIR = []
    for i in range(len(LIST_FILES)):
        FICHERO = open('DATOS/' + LIST_FILES[i], 'r')
        print('Leyentdo el fichero ' + LIST_FILES[i])
        DATOS = FICHERO.readlines()

        for n in range(int(float(len(DATOS)) / (N_CELLS + 1))):
            TIMELINE.append(
                datetime.datetime(int(DATOS[(N_CELLS + 1) * n].split()[2]), int(DATOS[(N_CELLS + 1) * n].split()[0]),
                                  int(DATOS[(N_CELLS + 1) * n].split()[1]), int(DATOS[(N_CELLS + 1) * n].split()[3]),
                                  int(DATOS[(N_CELLS + 1) * n].split()[4]), int(DATOS[(N_CELLS + 1) * n].split()[5])))
            ERROR_CD.append(float(DATOS[(N_CELLS + 1) * n].split()[6]))
            STATUS_CD.append(float(DATOS[(N_CELLS + 1) * n].split()[7]))
            BATT_VOL.append(float(DATOS[(N_CELLS + 1) * n].split()[8]))
            SOUND_SP.append(float(DATOS[(N_CELLS + 1) * n].split()[9]))
            HEADING.append(float(DATOS[(N_CELLS + 1) * n].split()[10]))
            PITCH.append(float(DATOS[(N_CELLS + 1) * n].split()[11]))
            ROLL.append(float(DATOS[(N_CELLS + 1) * n].split()[12]))
            PRESS.append(float(DATOS[(N_CELLS + 1) * n].split()[13]))
            WTEMP.append(float(DATOS[(N_CELLS + 1) * n].split()[14]))

            V_EAST.append([])
            V_NORTH.append([])
            V_UP.append([])
            AMP_B1.append([])
            AMP_B2.append([])
            AMP_B3.append([])
            V_SPEE.append([])
            V_DIR.append([])
            for m in range(N_CELLS):
                V_EAST[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[2]))
                V_NORTH[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[3]))
                V_UP[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[4]))
                AMP_B1[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[5]))
                AMP_B2[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[6]))
                AMP_B3[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[7]))
                V_SPEE[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[8]))
                V_DIR[n].append(float(DATOS[(N_CELLS + 1) * n + 1 + m].split()[9]))

        FICHERO.close()
        del DATOS

        V_EAST = np.array(V_EAST)
        V_NORTH = np.array(V_NORTH)
        V_UP = np.array(V_UP)
        AMP_B1 = np.array(AMP_B1)
        AMP_B2 = np.array(AMP_B2)
        AMP_B3 = np.array(AMP_B3)
        V_SPEE = np.array(V_SPEE)
        V_DIR = np.array(V_DIR)

    return TIMELINE, N_CELLS, DIST, ERROR_CD, STATUS_CD, BATT_VOL, SOUND_SP, HEADING, PITCH, ROLL, PRESS, WTEMP, V_EAST, V_NORTH, V_UP, AMP_B1, AMP_B2, AMP_B3, V_SPEE, V_DIR


########################################################################################################################
#
#
# 11? leeSBE37
def leeDataSBE37(DATADIR):
    import datetime
    TIMELINE = []
    NBITES = []
    WPRESS = []
    DEPTH = []
    WTEMP = []
    COND = []
    SALT = []
    SSPE = []

    # Busca la información eb en el fichero .cnv
    LIST_FILES = toolEncuentraEXT(DATADIR, '.cnv')
    for i in range(len(LIST_FILES)):
        FICHERO = open('DATOS/' + LIST_FILES[i], 'r')
        print('Leyentdo el fichero ' + LIST_FILES[i])
        DATOS = FICHERO.readlines()
        INTERVAL = DATOS[6]
        INTERVAL = int(INTERVAL[INTERVAL.find('=') + 1:INTERVAL.find('seconds')])
        INST_ID = DATOS[14]
        INST_ID = INST_ID[INST_ID.rfind("='") + 2:INST_ID.rfind("'")]

        for n in range(DATOS.index('*END*\n') + 1, len(DATOS)):
            TIMELINE.append(datetime.datetime.fromtimestamp(float(DATOS[n].split()[0]) + 946684800))
            NBITES.append(float(DATOS[n].split()[1]))
            WPRESS.append(float(DATOS[n].split()[2]))
            DEPTH.append(float(DATOS[n].split()[3]))
            WTEMP.append(float(DATOS[n].split()[4]))
            COND.append(float(DATOS[n].split()[5]))
            SALT.append(float(DATOS[n].split()[6]))
            SSPE.append(float(DATOS[n].split()[8]))
        FICHERO.close()
        del DATOS

    return INTERVAL, INST_ID, TIMELINE, NBITES, WPRESS, DEPTH, WTEMP, COND, SALT, SSPE


########################################################################################################################
#
#
# 12? leeTemHum FUNCION DE LECTURA DE DATOS
def leeBaro(DIR):
    import os
    import numpy as np
    from datetime import datetime

    # Prepara variables
    LIST_FILES = []
    TIMELINE = []
    PRESION = []

    # Lista con todos los ficheros del directorio:
    LIST_DIR = os.walk(DIR)  # os.walk()Lista directorios y ficheros
    # Crea una lista de los ficheros ail que existen en el directorio y los incluye a la lista.
    for root, dirs, files in LIST_DIR:
        for FILE in files:
            (FILE_NAME, EXT) = os.path.splitext(FILE)
            if (EXT == ".ail"):
                LIST_FILES.append(FILE_NAME + EXT)
        N_FILES = len(LIST_FILES)
        print("Se han encomntrado ", N_FILES, " ficheros en el directorio " + DIR)
    # Lee los datos
    for N in range(N_FILES):
        FILE = DIR + LIST_FILES[N]
        DATOS = np.genfromtxt(FILE, dtype=bytes).astype(str)
        PRESION.extend(list(map(float, DATOS[:, 3])))
        for i in range(len(DATOS)):
            TIMELINE.append(datetime.strptime(DATOS[i, 0] + ' ' + DATOS[i, 1], '%Y-%m-%d %H:%M:%S'))
        del FILE, DATOS
    return TIMELINE, PRESION


###############################################################################