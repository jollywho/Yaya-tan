#!/usr/bin/sh

#todo: send "done {file}" msg to YQS

#if file
if [ -f "${1}" ]; then
  data=$(basename "${1}" | eidata)
else
  data=${1}
fi

eiinsert ${data}
eidirpop "${1}" ${data}
