#!/usr/bin/sh

AWD=$(pwd)/
#if file
if [ -f "${1}" ]; then
  data=$(basename "${1}" | eidata)
  name=$(echo "$data" | cut -d ' ' -f1)
#if directory
else
  data=${1}
fi

eiinsert ${data}

if [ "$HOSTNAME" == casper ]; then
  EIIDIR='/usr/share/eii/lib'
elif [ "$HOSTNAME" = melchior ]; then
  EIIDIR='/mnt/eii/lib'
fi

EIICMD="./eii.sh"
cd ${EIIDIR}

aid=$(echo $res | cut -d '|' -f2)
secret=$(cat ${AWD}../../secret)
adata=$(ruby ${AWD}mal.rb ${secret[0]} ${secret[1]} "${name}")
ep=$(echo $adata | cut -d '|' -f1)
date=$(echo $adata | cut -d '|' -f2)
${EIICMD} -u -a -x -t master -c episodecount -f name -v ${name} -n ${ep}
${EIICMD} -u -a -x -t master -c date -f name -v ${name} -n ${date}

#!!debug disabled
#eidirpop "${1}" ${data}
