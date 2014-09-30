#! /usr/bin/env python
import socket,os,glob
import shlex

class Yaya_serv():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('casper', 8889))
        self.s.listen(1)
        self.hostpath = os.environ['HOME']
        self.fifopath = "%s/.weechat/weechat_fifo*"
        self.fifo = glob.glob(self.fifopath % self.hostpath)
        self.msg = "echo 'irc.%s.#%s *%s' > " + self.fifo[0]

    def retry_send(self):
        print(self.fspl)
        self.fspl[2] = self.fspl[2].replace("batch", "send")
        self.send(self.fspl)

    def send(self, spl):
        self.fspl = spl
        os.popen(self.msg % (spl[0], spl[1], spl[2]))

    def run(self):

        while 1:
            self.c, adrr = self.s.accept()
            data = self.c.recv(2048)
            if len(data) > 0:
                buf = data.decode("UTF-8")
                spl = shlex.split(buf)
                if spl[0] == '!':
                    self.retry_send()
                else:
                    self.send(spl)
