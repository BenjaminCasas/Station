#!/bin/bash

#Inicia los scripts de captura de datos
SCRIPT=$(readlink -f $0);
HOME=`dirname $SCRIPT`;

cd $HOME
pwd
source venv/bin/activate
python3 pythonCaptura.py&
TMP="${HOME%/*}"
STATION="${TMP##*/}"
INSTANT=$(date +%Y'-'%m'-'%d' '%H':'%M':'%S)
LOG=$HOME'/logs/LOG-'$STATION'.log'
LOG_TMP=$HOME'/logs/LOG-'$STATION'.TMP'
TEXT=$INSTANT' | LOG_ENV. Se ejecuta el script envioDAT.sh - USB'
echo $TEXT >> $LOG
tail -5000 $LOG > $LOG_TMP
mv $LOG_TMP $LOG
