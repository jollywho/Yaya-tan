#!/usr/bin/sh
transmission-show "${1}" | sed '1,/FILES/d'
