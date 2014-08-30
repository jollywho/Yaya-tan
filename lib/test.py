# -*- coding: utf-8 -*-
import socket

server = "irc.rizon.net"
channel = "#/g/sicp"
botnick = "Yaya-tan"

def ping():
  ircsock.send("PONG :Pong\n")

def sendmsg(chan , msg):
  ircsock.send("PRIVMSG " + chan +" :"+ msg +"\n") 

def joinchan(chan):
  ircsock.send("JOIN " + chan + "\n")

def hello(nick):
  ircsock.send("PRIVMSG "+ channel +" :今晩は " + nick + "さま!\n")

def commands(nick, channel, message):
    ircsock.send('PRIVMSG %s :%s お兄ちゃん\n' % (channel, message))
    #ircsock.send('PRIVMSG %s :%s お兄ちゃん\n' % (nick, message))

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER " + botnick + " " + botnick + " " + botnick + " :abc\n")
ircsock.send("NICK " + botnick + "\n")

joinchan(channel)

while 1:
    ircmsg = ircsock.recv(2048)
    ircmsg = ircmsg.strip('\n\r')

    print(ircmsg)
    #if ircmsg.find(' PRIVMSG ') != -1:
    #    nick = ircmsg.split('!')[0][1:]
    #    channel = ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
    #    msg = ircmsg.split(' PRIVMSG ')[-1].split(' :')[1]
    #    commands(nick, channel, msg)

    if ircmsg.find("Hello") != -1:
        nick = ircmsg.split('!')[0][1:]
        hello(nick)

    if ircmsg.find("PING :") != -1:
        ping()
