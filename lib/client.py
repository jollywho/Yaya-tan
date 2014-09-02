import socket
import os
def client():
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        os.remove("/tmp/aaa")
    except OSError:
        pass
    s.bind("/tmp/aaa")
    s.listen(1)

    while 1:
        c, adrr = s.accept()
        data = c.recv(2048)
        c.send(data)

#todo:  getopts

#todo:  default serv
#       default chan
client()
