#!/usr/bin/sh

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

EIICMD="${EIIDIR}/eii.sh"
dbdir=/home/chishiki/qp/einibl/anidb/bin/anidb.db
sql="-t titles -c type,aid,title -f title -v ${name}"
res=$(. ${EIICMD} -s -db $dbdir $sql)
echo $res
#if only a single record of type 1 exists
if [ $(echo "${res}" | grep "^1" | wc -l) -eq 1 ] || \
   [ $(echo "${res}" | wc -l) -eq 1 ]; then
    aid=$(echo $res | cut -d '|' -f2)
    ruby anidb.rb $aid
    #eii -u -x -t master -c episodecount -f name -v '${name}' -n adata0
    #eii -u -x -t master -c date -f name -v '${name}' -n adata1
else
  echo nothing found
fi

#!!debug disabled
#eidirpop "${1}" ${data}
