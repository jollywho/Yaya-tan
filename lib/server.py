#! /usr/bin/env python
import socketserver, subprocess, sys, os
from threading import Thread

HOST = 'localhost'
PORT = 2000

def pipe_command(data):
    return bytes('test', 'UTF-8')

class SingleTCPHandler(socketserver.BaseRequestHandler):
    "One instance per connection.  Override handle(self) to customize action."
    def handle(self):
        # self.request is the client connection
        data = self.request.recv(1024)  # clip input at 1Kb
        reply = pipe_command(data)
        if reply is not None:
            self.request.send(reply)
        self.request.close()

class SimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)

if __name__ == "__main__":

    stdin = '/dev/null'
    stdout = '/dev/null'
    stderr = '/dev/null'

    try:
        pid = os.fork( )
        if pid > 0:
            sys.exit(0) # Exit first parent.
    except OSError as e:
        sys.stderr.write("fork #1 failed: (%d) %sn" % (e.errno, e.strerror))
        sys.exit(1)
    # Decouple from parent environment.
    os.chdir("/")
    os.umask(0)
    os.setsid( )
    # Perform second fork.
    try:
        pid = os.fork( )
        if pid > 0:
            sys.exit(0) # Exit second parent.
    except OSError as e:
        sys.stderr.write("fork #2 failed: (%d) %sn" % (e.errno, e.strerror))
        sys.exit(1)

    for f in sys.stdout, sys.stderr: f.flush( )
    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'a+')
    os.dup2(si.fileno( ), sys.stdin.fileno( ))
    os.dup2(so.fileno( ), sys.stdout.fileno( ))
    os.dup2(se.fileno( ), sys.stderr.fileno( ))


    server = SimpleServer((HOST, PORT), SingleTCPHandler)
    # terminate with Ctrl-C
    while True:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            sys.exit(0)
