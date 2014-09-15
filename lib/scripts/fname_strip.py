import sys
import re
name = sys.stdin.read()
rep = re.sub("\[.*?\]", "", name)
ismatch = re.match("(.+[^Ep]).*[_ -]([-0-9]{5})", rep)

if ismatch != None:
    title = re.sub("[_ -]", "_", ismatch.groups()[0])
    title = re.sub("^_", "", title)
    title = re.sub("__", "", title)
    ep = re.sub("[_ ]", "", ismatch.groups()[1])
    print(title)
    print(ep)
else:
    ismatch = re.match("(.+[^Ep]).*[_ -]([-0-9]{2,4})", rep)
    if ismatch != None:
        title = re.sub("[_ -]", "_", ismatch.groups()[0])
        title = re.sub("^_", "", title)
        title = re.sub("__", "", title)
        ep = re.sub("[_ ]", "", ismatch.groups()[1])
        print(title)
        print(ep)
