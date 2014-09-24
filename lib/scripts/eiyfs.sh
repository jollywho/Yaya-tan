#!/usr/bin/sh

data=$(basename "${1}" | eidata)
eiinsert ${data}
eidirpop "${1}" ${data}
