einibl $@

pipe=/tmp/einibl.tmp

if [ -f $pipe ];then
  cat $pipe | python req_dcc.py
  rm $pipe
fi
