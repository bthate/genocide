# This file is placed in the Public Domain.


"thread"


import threading
import time


from hx.cmd import Commands
from hx.obj import Object, get, update
from hx.run import starttime
from hx.utl import elapsed


def reg():
    Commands.add(thr)


def rem():
    Commands.remove(thr)


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
