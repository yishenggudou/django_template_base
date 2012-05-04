#!/bin/bash


# Replace these three settings.
PROJDIR=`pwd`
PIDFILE="$PROJDIR/www.pid"
SOCKET="$PROJDIR/www.sock"
echo ${PROJDIR}
cd $PROJDIR
if [ -f $PIDFILE ]; then
	kill -9 `cat  $PIDFILE`
	rm -f -- $PIDFILE
fi
#cd $PROJDIR && /usr/local/python2.7/bin/python2.7 manage.py runfcgi method=threaded host=127.0.0.1 port=8016 pidfile=$PIDFILE outlog=rout.log errlog=rerr.log
cd $PROJDIR && sudo /usr/local/python2.7/bin/python2.7 manage.py runfcgi method=threaded host=127.0.0.1 port=7171 pidfile=$PIDFILE outlog="${PROJDIR}rout.log" errlog="${PROJDIR}err.log"

