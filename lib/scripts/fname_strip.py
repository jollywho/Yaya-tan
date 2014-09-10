import sys
import re
name = sys.stdin.read()
print(name)
ismatch = re.match("(?:\[.*?\])?[_ ]?(.+).*?(?:[_ -][0-9]{1,3}).*(?:\[.*?\])?", name)
if ismatch != None:
    strip = re.match("(.+)[_ -].+", ismatch.groups()[0])
    if strip != None:
        print(strip.groups()[0])
    else:
        print(ismatch.groups()[0])
