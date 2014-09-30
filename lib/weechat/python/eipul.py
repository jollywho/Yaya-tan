import weechat as wc
import socket
import os

wc.register("eipsh", "chishiki", "0.0", "GPL3", "all teh dcc things", "", "")

process_output = ""

def send_message(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("casper", 8889))
    s.send("!")

def batch_unsupported(data, signal, signal_data):
    if "unsupported" in signal_data:
        send_message("!")
    return wc.WEECHAT_RC_OK

def xfer_end_do(data, signal, signal_data):
    wc.infolist_next(signal_data)
    status = wc.infolist_string(signal_data, 'status_string')
    filename = wc.infolist_string(signal_data, 'filename')
    local = wc.infolist_string(signal_data, 'local_filename')
    print(status)
    if status == "done":
        os.popen('eiyfs "%s"' % local, 'r', 0)
    return wc.WEECHAT_RC_OK

wc.hook_signal("weechat_pv", "batch_unsupported", "")
wc.hook_signal("xfer_ended", "xfer_end_do", "")
