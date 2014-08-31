import socket
def client():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect("/tmp/aaa")
    sock.send(b"test")
    reply = sock.recv(14)  # limit reply to 16K
    sock.close()
    return reply

print(client().decode('utf-8'))
