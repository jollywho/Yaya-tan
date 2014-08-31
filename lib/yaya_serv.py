#! /usr/bin/env python
import socketserver, subprocess, sys, os
from threading import Thread

HOST = 'localhost'
PORT = 2000

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

class Yaya_serv():
    def __init__(self):
        self.server = SimpleServer((HOST, PORT), SingleTCPHandler)

    def pipe_command(data):
        return bytes('test', 'UTF-8')


    def run(self):
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            sys.exit(0)
