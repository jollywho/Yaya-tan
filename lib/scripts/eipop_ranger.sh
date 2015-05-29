#!/usr/bin/sh

find "$@" -iname '*.*' | while read file;
do
  eiyfs "$file"
done
