#!/usr/bin/sh
einibl $@

pipe=/tmp/einibl.tmp

if [ -f $pipe ];then
  cat $pipe | req_dcc
  rm $pipe
fi
