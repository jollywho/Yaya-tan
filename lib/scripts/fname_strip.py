import sys
import re
name = sys.stdin.read()
rep = re.sub("\[.*?\]", "", name)
ismatch = re.match("(.+).*([_ -][0-9]{2,3}[v0-9]?)", rep)

if ismatch != None:
    title = re.sub("[_ -]", "", ismatch.groups()[0])
    ep = re.sub("[_ -]", "", ismatch.groups()[1])
    print(title)
    print(ep)
