#!/usr/bin/python
import sys
import re

opt = ''.join(sys.argv[1:])
name = sys.stdin.read()

subgroup = re.search("\[(.*?)\]", name)
subgroup = subgroup.group(1) if subgroup != None else ""

checksum = re.search("[\[|\(]([0-f]{8})[\]|\)]", name)
checksum = checksum.group(1) if checksum != None else ""

rep = re.sub("\[.*?\]", "", name)
rep = re.sub("\(.*?\)", "", rep)

match_type = \
        [
        "(.+[^Ep][^_-]).*[._ -]Ep([0-9]{2,3})",
        "(.+[^_-]).*[._ -]([Ss][0-9]{2}[Ee][0-9]{2})",
        "(.+[^Ep][^_-]).*[._ -]([0-9]{2,3}-[0-9]{2,3})",
        "(.+[^Ep][^_-]).*[._ -]([0-9]{2,3})",
        "(.+[^_-]).*[._ -]([0-9]{1,2}[Xx][0-9]{1,2})",
        "(.+[^Ep][^_-]).*([0-9]{2,3})",
        "(.+[^Ep][^_-]).*(ED|OP[0-9]{1,2})",
        "(.+[^Ep][^_-]).*_-_.*()",
        ]

def output(title,ep,subgroup,checksum):
    if not (opt):
        print(title, " ", ep, " ", subgroup, " ", checksum)
    else:
        if (opt == "-title"): print(title)
        if (opt == "-ep"): print(ep)
        if (opt == "-subgroup"): print(subgroup)
        if (opt == "-checksum"): print(checksum)

def pull(m):
    title = re.sub("[._ ]", "_", m.groups()[0])

    tmv = re.split("(^_?[T|t]he)", title)
    if len(tmv) > 2:
        title = tmv[2] + ",the"

    title = re.sub("^_", "", title)
    title = re.sub("__", "", title)
    title = re.sub("_$", "", title)
    ep = re.sub("[_ ]", "", m.groups()[1])
    output(title.title(), ep, subgroup, checksum)

def do_match(x):
    m = re.match(match_type[x], rep)
    if m != None:
        pull(m)
    else:
        do_match(x+1) if x+1 < len(match_type) else None

do_match(0)
