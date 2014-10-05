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

#!!debug disabled
#eiinsert ${data}

if [ "$HOSTNAME" == casper ]; then
  EIIDIR='/usr/share/eii/lib'
elif [ "$HOSTNAME" = melchior ]; then
  EIIDIR='/mnt/eii/lib'
fi

EIICMD="./eii.sh"
dbdir=/home/chishiki/qp/einibl/anidb/bin/anidb.db

cd ${EIIDIR}

sql="-t titles -c type,aid,title -f title -v ${name}"
res=$(${EIICMD} -s -db $dbdir $sql)

#if only a single record of type 1 exists
if [ $(echo "${res}" | grep "^1" | wc -l) -eq 1 ] || \
   [ $(echo "${res}" | wc -l) -eq 1 ]; then
    aid=$(echo $res | cut -d '|' -f2)
    adata=$(ruby ${AWD}anidb.rb $aid)
    ep=$(echo $adata | cut -d '|' -f1)
    date=$(echo $adata | cut -d '|' -f2)
    ${EIICMD} -u -a -x -t master -c episodecount -f name -v ${name} -n ${ep}
    ${EIICMD} -u -a -x -t master -c date -f name -v ${name} -n ${date}
else
  echo nothing found
fi

#!!debug disabled
#eidirpop "${1}" ${data}
