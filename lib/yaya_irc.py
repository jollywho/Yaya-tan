#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
server = "irc.rizon.net"
channel = "#yayatest"
botnick = "Yaya-tan"

class Yaya_irc():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((server, 6667))
        msg = "USER " + botnick + " " + botnick + " " + botnick + " :#\n"
        self.s.send(bytes(msg, "UTF-8"))
        msg = "NICK " + botnick + "\n"
        self.s.send(bytes(msg, "UTF-8"))
        self.joinchan(channel)

    def ping(self):
      self.s.send(bytes("PONG :Pong\n", "UTF-8"))

    def sendmsg(self, chan , msg):
      self.s.send(bytes("PRIVMSG " + chan +" :"+ msg +"\n", "UTF-8"))

    def joinchan(self, chan):
      self.s.send(bytes("JOIN " + chan + "\n", "UTF-8"))

    def hello(self, nick):
      self.s.send(bytes("PRIVMSG "+ channel +" :今晩は " + nick + "さま!\n", "UTF-8"))

    def commands(self, nick, channel, message):
      self.s.send(bytes('PRIVMSG %s :%s お兄ちゃん\n' % (channel, message), "UTF-8"))

    def run(self):

        while 1:
            data = self.s.recv(2048)
            data = data.decode('utf-8').strip('\n\r')

            if data.find("#test#") != -1:
                nick = data.split('!')[0][1:]
                self.hello(nick)

            if data.find("PING :") != -1:
                ping()
