import sys
import re
name = sys.stdin.read()
ismatch = re.match("(?:\[.*?\])?[_ ]?(.+).*?([_ -][0-9]{1,3}).*(?:\[.*?\])?", name)
if ismatch != None:
    title = re.match("(.+)[_ -].+", ismatch.groups()[0])
    ep = re.match("[_ -]*(.+)[_ -]*", ismatch.groups()[1])
    if title != None:
        print(title.groups()[0])
    else:
        print(ismatch.groups()[0])
    if ep != None:
        print(ep.groups()[0])
