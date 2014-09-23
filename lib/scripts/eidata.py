#!/usr/bin/python
import sys
import re

name = sys.stdin.read()
subgroup = re.search("\[(.*?)\]", name).group(1)
checksum = re.search("[\[|\(]([0-f]{8})[\]|\)]", name).group(1)
rep = re.sub("\[.*?\]", "", name)
rep = re.sub("\(.*?\)", "", rep)

match_type = \
        [
        "(.+[^Ep]).*[._ -]([0-9]{2,3}-[0-9]{2,3})",
        "(.+[^Ep]).*[._ -]([0-9]{2,3})",
        "(.+).*[._ -]([Ss][0-9]{2}[Ee][0-9]{2})",
        "(.+).*[._ -]([0-9]{1,2}[Xx][0-9]{1,2})",
        "(.+[^Ep]).*([0-9]{2,3})",
        "(.+[^Ep]).*(ED|OP[0-9]{1,2})",
        ]

def pull(m):
    title = re.sub("[._ -]", "_", m.groups()[0])

    tmv = re.split("(^_?The)", title)
    if len(tmv) > 2:
        title = tmv[2] + "," + tmv[1]

    title = re.sub("^_", "", title)
    title = re.sub("__", "", title)
    title = re.sub("_$", "", title)
    ep = re.sub("[_ ]", "", m.groups()[1])
    print(title.title(), " ", ep, " ", subgroup, " ", checksum)

def do_match(x):
    m = re.match(match_type[x], rep)
    if m != None:
        pull(m)
    else:
        do_match(x+1) if x+1 < len(match_type) else None

do_match(0)
