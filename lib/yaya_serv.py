#! /usr/bin/env python
import socket,os,glob

class Yaya_serv():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('casper', 8889))
        self.s.listen(1)
        self.hostpath = os.environ['HOME']

    def run(self):

        while 1:
            self.c, adrr = self.s.accept()
            data = self.c.recv(2048)
            if len(data) > 0:
                buf = data.decode("UTF-8")
                msg = "echo 'irc.rizon.#yayatest"
                msg += " *%s'" % data.decode("UTF-8").strip()
                fl = glob.glob("%s/.weechat/weechat_fifo*" % self.hostpath)
                msg += " > %s" % fl[0]
                os.popen(msg)

