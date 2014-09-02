#! /usr/bin/env python
import socket,os

class Yaya_dcc():
    def __init__(self, ip, port, size):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ip = hex(int(ip))[2::1]
        hp = ""
        for x in range(0, 8, 2):
            hp += str(int(ip[x:x+2], 16)) + "."
        self.host = hp[0:-1]
        self.port = port
        self.size = size

    def conn(self):
        res = None
        while res is None:
            try:
                res = self.s.bind(("", int(self.port)))
                res = self.s.listen(1)
            except:
                pass
        self.run()

    def run(self):

        while 1:
            self.conn, addr = self.s.accept()
            data = None
            try:
                data = self.conn.recv(1024)
            except Exception as e:
                print(e)
            print(data) if data != None else None

#            if ircmsg.find("#test#")!= -1:
#                nick = ircmsg.split('!')[0][1:]
#                self.hello(nick)
#
#            if ircmsg.find("PING :") != -1:
#                ping()
