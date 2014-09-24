#!/usr/bin/sh

#a) YFS (eidrp)  -> EII
#b) YFS (eiatrm) -- {file}
#c) YFS (dirpop) -> YayaFS

data=$(basename "${1}" | eidata)
eiinsert ${data}
eidirpop "${1}" ${data}
