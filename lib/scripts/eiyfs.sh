#!/usr/bin/sh

#if file
if [ -f "${1}" ]; then
  data=$(basename "${1}" | eidata)
#if directory
else
  data=${1}
fi

eiinsert ${data}
eidirpop "${1}" ${data}
