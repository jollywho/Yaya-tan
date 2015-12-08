#!/usr/bin/sh

trap "exit 0" SIGINT

if [ $# -eq 0 ]; then
  exit
fi

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
#file
elif [ $1 = '--file' ]; then
  einibl $(echo "${@:2}" | eidata -title)
#kill
elif [ $1 = '--kill' ]; then
  msg="-s yaya -c ; -m 'kill'"
  echo -e "$msg" | req_dcc
#do search
else
  einibl $@
fi
