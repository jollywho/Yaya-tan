import sys
import re
name = sys.stdin.read()
print(name)
print(re.match("(?:\[.*?\])?[_ ]?(.+)(?:[_ -])+?.*?(?:[_ -][0-9]{1,3}).*(?:\[.*?\])?", name).groups()[0])
