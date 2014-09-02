import socket
import os,sys
import getopt

server = " "
channel = " "
message = " "

def send_message(server, channel, message):
    msg = " ".join([server, channel, message])
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
        c.send(bytes(msg, "utf-8"))

def main(argv):
    msg = argv
    global server
    global channel
    global message
    try:
        opts, args = getopt.getopt(argv,"hs:c:m:",
                ["server=","channel=","message="])
    except getopt.GetoptError:
        print('test.py -s <server> -c <channel> -m <message>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py [--server=] [--chanel=] [--message=]')
            sys.exit()
        elif opt in ("-s", "--server"):
            server = arg
            msg.remove("-s")
            msg.remove(arg)
        elif opt in ("-c", "--channel"):
            channel = arg
            msg.remove("-c")
            msg.remove(arg)
        elif opt in ("-m", "--message"):
            message = arg
            msg.remove("-m")
            msg.remove(arg)
    return msg

if __name__ == "__main__":
    msg = main(sys.argv[1:])
    message = ''.join(msg) if message is " " else message
    print("server: %s" % server)
    print("channel: %s" % channel)
    print("message: %s" % message)
    send_message(server, channel, message)
