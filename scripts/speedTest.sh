VER='2022-05-27 bcasas@socib.es' #Actualización del scipt para que funcione con la nueva versión de speedtest
#VER='2020-10-13 bcasas@socib.es' #Archiva el resultado en WAN
UMBRAL_PING=100
UMBRAL_UPLOAD=1
UMBRAL_DOWNLOAD=1

STATION='Station'

INSTANT=$(date +%Y'-'%m'-'%d' '%H':'%M':'%S)
MES=$(date +%Y%m)
SCRIPT=$(readlink -f $0);
DIR_SCRIPTS=`dirname $SCRIPT`;
DIR_ROOT="${DIR_SCRIPTS%/*}"
DIR_LOG=$DIR_SCRIPTS'/logs/'
if [ ! -d $DIR_LOG ];
    then
    mkdir $DIR_LOG
fi
LOG_FILE=$DIR_LOG'LOG-'$STATION'.log'
SPE_FILE=$DIR_LOG'SPE-'$STATION'.log'
TMP_FILE=$DIR_LOG'SPE-'$STATION'.TMP'

DIR_WAN=$DIR_ROOT'/WAN/'
if [ ! -d $DIR_WAN ];
then
mkdir $DIR_WAN
fi
DIR_WAN_rI=$DIR_WAN'rawInput/'
if [ ! -d $DIR_WAN_rI ];
then
mkdir $DIR_WAN_rI
fi
DIR_WAN_rA=$DIR_WAN'rawArchive/'
if [ ! -d $DIR_WAN_rA ];
then
mkdir $DIR_WAN_rA
fi
if [ $(date +%d) -eq 01 ] 
then
    mv $DIR_WAN_rI * $DIR_WAN_rA
fi

FILE_AIL=$DIR_WAN_rI$MES'_'$STATION'.ail'


if [ -f $SPE_FILE ];
    then
    #echo 'el fichero '$SPE_FILE' existe. Hago el tail'
    tail -18 $SPE_FILE > $TMP_FILE
    mv $TMP_FILE $SPE_FILE
fi

if [ -f $TMP_FILE ];
    then
    rm $TMP_FILE
fi

/usr/bin/speedtest-cli --share >> $TMP_FILE

TEXT=$INSTANT' | LOG_SPE. Se realiza un test de velocidad'
echo $TEXT >> $LOG_FILE

echo $INSTANT >> $SPE_FILE
CONTADOR=1
while read linea; do
    #echo 'CONTADOR='$CONTADOR'    linea='$linea;
    if [ $CONTADOR = 2 ]
    then 
        TEXT=$linea
        echo $TEXT >> $SPE_FILE
    fi
    if [ $CONTADOR = 5 ]
    then 
        TEXT=$linea
        echo $TEXT >> $SPE_FILE
        PING=${TEXT#*]:}
        PING=${PING% ms*}
    fi
    if [ $CONTADOR = 7 ]
    then 
        TEXT=$linea
        echo $TEXT >> $SPE_FILE
        SUBIDA=${TEXT##*:}
        SUBIDA=${SUBIDA% *}
    fi
    if [ $CONTADOR = 9 ]
    then 
        TEXT=$linea
        echo $TEXT >> $SPE_FILE
        BAJADA=${TEXT##*Download}
        BAJADA=${BAJADA#*:}
        BAJADA=${BAJADA%% Mbit*}
    fi
    if [ $CONTADOR = 10 ]
    then 
        TEXT=$linea
        echo $TEXT >> $SPE_FILE
    fi
    CONTADOR=$((CONTADOR+1))
done < $TMP_FILE

if [ $CONTADOR -lt 10 ]
 then
    TEXT='NoHTTP'
    echo $TEXT >> $SPE_FILE
fi


#echo 'PING='$PING
#echo 'SUBIDA='$SUBIDA
#echo 'BAJADA='$BAJADA
TEXT=$INSTANT' |  Ping='$PING'ms   Bajada='$BAJADA'Mbit   Subida='$SUBIDA'Mbit'
echo $TEXT>>$FILE_AIL
rm $TMP_FILE


mensaje=''
tipo='SPE'
TST=${PING%%.*}
if [ $TST -gt $UMBRAL_PING ]
then
    mensaje='La latencia de la conexion a internet es ALTA. Ping:'$PING'ms (umbral = '$UMBRAL_PING'ms), Upload:'${SUBIDA}'Mbit/s, Download:'${BAJADA}'Mbit/s'
fi

TST=${SUBIDA%%.*}
if [ $TST -lt $UMBRAL_UPLOAD ]
then
    if [ ! -z "$mensaje" ]
    then 
        mensaje='La latencia de la conexion a internet es ALTA y la velocidad de subida es BAJA. Ping:'$PING'ms (umbral = '$UMBRAL_PING'ms) , Upload:'${SUBIDA}'Mbit/s (umbral = '$UMBRAL_UPLOAD'Mbit/s), Download:'${BAJADA}'Mbit/s'
    else
        mensaje='La velocidad de subida de la conexión de conexión a internet es BAJA. Upload:'${SUBIDA}'Mbit/s (umbral = '$UMBRAL_UPLOAD'Mbit/s), Download:'${BAJADA}'Mbit/s, Ping:'$PING'ms'
    fi
fi

TST=${BAJADA%%.*}
if [ $TST -lt $UMBRAL_DOWNLOAD ]
then
    if [ ! -z "$mensaje" ]
    then
        mensaje=${mensaje}'. La velocidad de descarga de la conexión de conexión a internet BAJA.'
        else
        mensaje='La velocidad de descarga de la conexión de conexión a internet BAJA. Download:'${BAJADA}'Mbit/s (umbral = '$UMBRAL_DOWNLOAD'Mbit/s), Upload:'${SUBIDA}'Mbit/s, Ping:'$PING'ms'
    fi
fi


if [ ! -z "$mensaje" ]
then
    python3 pythonNotifica.py ${tipo} "${mensaje}"
fi
