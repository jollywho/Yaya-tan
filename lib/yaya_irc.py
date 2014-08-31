#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import threading
import socketserver
server = "irc.rizon.net"
channel = "#yayatest"
botnick = "Yaya-tan"

class Yaya_irc():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((server, 6667))
        msg = "USER " + botnick + " " + botnick + " " + botnick + "\n"
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

        ircmsg = self.s.recv(2048)
        ircmsg = ircmsg.strip(bytes('\n\r', "UTF-8"))

        print(ircmsg)

        if ircmsg.find(bytes("#test#", "UTF-8"))!= -1:
            nick = ircmsg.split('!')[0][1:]
            hello(nick)

        if ircmsg.find(bytes("PING :", "UTF-8")) != -1:
            ping()
