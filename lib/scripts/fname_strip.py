import sys
import re
name = sys.stdin.read()
print(name)
ismatch = re.match("(?:\[.*?\])?[_ ]?(.+)(?:[_ -])+?.*?(?:[_ -][0-9]{1,3}).*(?:\[.*?\])?", name)
print(ismatch.groups()[0]) if ismatch != None else None
