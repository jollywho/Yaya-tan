import socket
import os,sys
import getopt
import shlex

server = " "
channel = " "
message = " "

def send_message(server, channel, message):
    msg = " ".join([server, channel, message])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("casper", 8889))
    s.send(bytes(msg, "UTF-8"))

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
            message = "'%s'" % arg
            msg.remove("-m")
            msg.remove(arg)
    return msg

if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = main(sys.argv[1:])
    else:
        args = shlex.split(sys.stdin.readline())
        msg = main(args)
    message = ''.join(msg) if message is " " else message
    send_message(server, channel, message)
