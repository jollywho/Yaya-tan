import weechat as wc
import socket

wc.register("eipsh", "chishiki", "0.0", "GPL3", "all teh dcc things", "", "")

process_output = ""

def listen(data, rem_calls):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect("/tmp/aaa")
    sock.send(b"test")

    fullmsg = sock.recv(1024)
    serv = fullmsg.split(" ")[0]
    chan = fullmsg.split(" ")[1]
    msg = fullmsg.split(" ")[2]

    wc.prnt("", fullmsg)

    sock.close()

    #buff = wc.info_get("irc_buffer", "rizon,#")
    #wc.command(buff, msg)
    return wc.WEECHAT_RC_OK

wc.hook_timer(5 * 1000, 0, 0, "listen", "test")
