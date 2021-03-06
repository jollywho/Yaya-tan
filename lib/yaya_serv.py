#!/usr/bin/env python
import socket,os,glob,sys
import shlex

class Yaya_serv():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('casper', 8889))
        self.s.listen(1)
        self.hostpath = os.environ['HOME']
        self.fifopath = "%s/.weechat/weechat_fifo*"
        self.fifo = glob.glob(self.fifopath % self.hostpath)
        if len(self.fifo) < 1:
            print("Error: weechat fifo not found. Cannot start.")
            sys.exit(1)
        else:
            self.msg = "echo '%s%s *%s' > " + self.fifo[0]

    def retry_send(self):
        if self.fspl[2].find("batch") != -1:
            self.fspl[2] = self.fspl[2].replace("batch", "send")
            self.send(self.fspl)

    def send(self, spl):
        self.fspl = spl
        spl[1] = spl[1].replace(";", "")
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
                elif spl[2] == "kill":
                    sys.exit(1)
                else:
                    self.send(spl)
