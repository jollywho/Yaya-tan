#! /usr/bin/env python
import socket,os

class Yaya_serv():
    def __init__(self):
        self.s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            os.remove("/tmp/aaa")
        except OSError:
            pass
        self.s.bind("/tmp/aaa")
        self.s.listen(1)

    def run(self):

        while 1:
            self.c, adrr = self.s.accept()
            data = self.c.recv(2048)
            self.c.send(data)

#            if ircmsg.find("#test#")!= -1:
#                nick = ircmsg.split('!')[0][1:]
#                self.hello(nick)
#
#            if ircmsg.find("PING :") != -1:
#                ping()
