#!/usr/bin/sh

#[l]ist xfers
if [ $1 = "-l" ]; then
  (yqs_get) &
  host=$(ip route get 8.8.8.8 | head -1 | cut -d' ' -f8)
  msg="-s core.weechat -c ; -m '/yqs_xfer -l ${host}:3333'"
  echo -e "$msg" | req_dcc
  wait
#[c]lose file xfer
elif [ $1 = '-c' ]; then
  msg="-s xfer.xfer.list -c ; -m 'c'"
  echo -e "$msg" | req_dcc
#[p]urge
elif [ $1 = '-p' ]; then
  msg="-s xfer.xfer.list -c ; -m 'p'"
  echo -e "$msg" | req_dcc
#do search
else
  einibl $@
fi

pipe=/tmp/einibl.tmp

if [ -f $pipe ]; then
  cat $pipe | req_dcc
  rm $pipe
fi
