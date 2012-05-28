#!/bin/bash


# Replace these three settings.
PROJDIR=`pwd`
PIDFILE="$PROJDIR/www.pid"
SOCKET="$PROJDIR/www.sock"
PORT="7171"
echo ${PROJDIR}
cd $PROJDIR
if [ -f $PIDFILE ]; then
	kill -9 `cat  $PIDFILE`
	rm -f -- $PIDFILE
fi
#cd $PROJDIR && sudo /usr/local/python2.7/bin/python2.7 manage.py runfcgi method=threaded host=127.0.0.1 port=${PORT} pidfile=${PIDFILE} outlog="${PROJDIR}rout.log" errlog="${PROJDIR}err.log"
cd $PROJDIR && sudo python manage.py runfcgi method=threaded host=127.0.0.1 port=${POR} pidfile=${PIDFILE} outlog="${PROJDIR}rout.log" errlog="${PROJDIR}err.log"

