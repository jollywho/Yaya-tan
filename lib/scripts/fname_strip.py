import sys
import re

name = sys.stdin.read()
rep = re.sub("\[.*?\]", "", name)
rep = re.sub("\(.*?\)", "", rep)

match_type = \
        ["(.+[^Ep]).*[._ -]([-0-9]{5})",
        "(.+[^Ep]).*[._ -]([-0-9]{2,4})",
        "(.+[^Ep])([-0-9]{2,4})"]

def pull(m):
    title = re.sub("[._ -]", "_", m.groups()[0])
    title = re.sub("^_", "", title)
    title = re.sub("__", "", title)
    ep = re.sub("[_ ]", "", m.groups()[1])
    print(title)
    print(ep)

def do_match(x):
    m = re.match(match_type[x], rep)
    if m != None:
        pull(m)
    else:
        do_match(x+1) if x+1 < len(match_type) else None

do_match(0)
