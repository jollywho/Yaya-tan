import os,sys,threading
from yaya_irc import Yaya_irc
from yaya_serv import Yaya_serv

def daemonize():
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

if __name__ == "__main__":

    daemonize()
    yaya = Yaya_irc()
    server = Yaya_serv()
    server.run()
    v = threading.Thread(target=server.run)
    v.daemon = True
    v.start()
    yaya.run()
