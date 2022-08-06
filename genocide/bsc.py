# This file is placed in the Public Domain.


"basic"


import threading
import time


from gd.obj import Object, get, update
from gd.run import Commands, starttime
from gd.utl import elapsed


def cmd(event):
    event.reply(",".join(sorted(Commands.cmd)))


def thr(event):
    result = []
    for t in sorted(threading.enumerate(), key=lambda x: x.getName()):
        if str(t).startswith("<_"):
            continue
        o = Object()
        update(o, vars(t))
        if get(o, "sleep", None):
            up = o.sleep - int(time.time() - o.state.latest)
        else:
            up = int(time.time() - starttime)
        result.append((up, t.getName()))
    res = []
    for up, txt in sorted(result, key=lambda x: x[0]):
        res.append("%s/%s" % (txt, elapsed(up)))
    if res:
        event.reply(" ".join(res))
    else:
        event.reply("no threads running")