import weechat as wc
import socket
import os

C_HOST = "casper"
C_PORT = 8889

wc.register("yqs_xfer", "chishiki", "1.0", "GPL3", "all teh dcc things", "", "") 
wc.hook_command("yqs_xfer",
         "run all the things that go ping",
         "[-l]",
         "...",
         "-l",
         "run","")

def send_message(host,port,msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(msg)

def request(ip,port):
    infolist = wc.infolist_get("xfer", "", "")
    name = ""
    if infolist:
      while wc.infolist_next(infolist):
         name += wc.infolist_string(infolist, "filename")
         name += " "
         name += wc.infolist_string(infolist, "status_string")
         name += " "
         name += wc.infolist_string(infolist, "bytes_per_sec")
         name += " "
         name += wc.infolist_string(infolist, "eta")
         name += " "
         name += wc.infolist_string(infolist, "pos")
         name += " "
         name += wc.infolist_string(infolist, "size")
         name += "|"
      name = name[:-1]
      wc.infolist_free(infolist)
      send_message(ip, port, name)

def run(data, buffer, args):
    if args[0:2] == "-l":
        ip,port = args[2:].split(":")
        port = int(port)
        request(ip,port)
    return wc.WEECHAT_RC_OK

def xfer_end_do(data, signal, signal_data):
    wc.infolist_next(signal_data)
    status = wc.infolist_string(signal_data, 'status_string')
    filename = wc.infolist_string(signal_data, 'filename')
    local = wc.infolist_string(signal_data, 'local_filename')
    if status == "done":
        os.popen('eiyfs "%s"' % local, 'r', 0)
    return wc.WEECHAT_RC_OK

def batch_unsupported(data, signal, signal_data):
    if "unsupported" in signal_data:
        send_message(C_HOST, C_PORT, "!")
    return wc.WEECHAT_RC_OK

wc.hook_signal("weechat_pv", "batch_unsupported", "")
wc.hook_signal("xfer_ended", "xfer_end_do", "")
