#!/bin/bash

#Detiene todos los procesos pyton en ejecucion 
kill -9 `ps -ef|grep -v grep |grep pythonCaptura| awk '{print $2}'`

#Inicia los scripts de captura de datos
SCRIPT=$(readlink -f $0);
HOME=`dirname $SCRIPT`;

cd $HOME
pwd
echo python3 pythonCaptura.py&
python3 pythonCaptura.py&
TMP="${HOME%/*}"
STATION="${TMP##*/}"
INSTANT=$(date +%Y'-'%m'-'%d' '%H':'%M':'%S)
LOG=$HOME'/logs/LOG-'$STATION'.log'
LOG_TMP=$HOME'/logs/LOG-'$STATION'.TMP'
TEXT=$INSTANT' | LOG_RNC. Se ejecuta el script reiniciaCaptura.sh'
echo $TEXT >> $LOG
tail -5000 $LOG > $LOG_TMP
mv $LOG_TMP $LOG
