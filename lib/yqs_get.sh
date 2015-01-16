#!/usr/bin/env python
import socket,os

#todo: capture errors from nibl. display in -[s]tatus
    #-command is unsupported
    #-invalid pack number
#todo: record requested files to yaya -[q]ueue
    #-clear queue with -qc

#todo: YQS getopts

#todo: 

#YQS [search str]
#YQS [l|s|q] | [p|r|c]
#    <option>  <command>
class col:
    WHITE = '\033[37m'
    RED = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ORANGE = '\033[91m'
    URED = '\033[4;31m'
    DARK = '\033[1;37m'
    BLACK = '\033[0;30m'
    PBOX = '\033[5;43;35m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    SOFF = ORANGE
    POFF = BLUE
    SON = GREEN
    PON = PBOX + RED
    AON = URED
    AOFF = BLACK

def fmt(msg):
    spl = msg.split(" ")

    name = spl[0]
    status = spl[1]
    rate = spl[2]
    eta = spl[3]
    pos = "%.2f" % (float(spl[4])/1024.0**2)
    size = "%.2f" % (float(spl[5])/1024.0**2)

    percent = "%2d" % (float(pos)/float(size)*100)
    if status == "done" or status == "aborted":
        stat_col = col.SOFF
        per_col = col.POFF
        act_col = col.AOFF
    else:
        stat_col = col.SON
        per_col = col.PON
        act_col = col.AON

    a = act_col + status + col.ENDC
    b = col.RED + "%.1f" % (float(rate)/1024.0) + col.ENDC
    c = stat_col + pos + col.ENDC
    d = col.SOFF + size + col.ENDC
    e = per_col + percent + "%" + col.ENDC

    z = col.DARK + "//" + col.ENDC
    m = col.DARK + "MB" + col.ENDC
    r = col.DARK + "KB/s" + col.ENDC

    print(col.YELLOW + name + col.ENDC)
    print("--> %s %s [%s%s%s%s] (%s%s)" % (a,e, c, z, d, m, b, r))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 3333))
s.listen(10)
c, adrr = s.accept()
data = c.recv(2048)
buf = data.decode("UTF-8")
for r in buf.split("|"):
    fmt(r)
c.close()
