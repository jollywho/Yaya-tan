#! /usr/bin/env python
import socket,os

class Yaya_serv():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind('casper', 8889)
        self.s.listen(1)

    def run(self):

        while 1:
            self.c, adrr = self.s.accept()
            data = self.c.recv(2048)
            if len(data) > 0:
                buf = buf.decode("UTF-8")
                print(buf)
