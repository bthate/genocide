# This file is placed in the Public Domain.

import threading
import time

from gcd.dbs import find, last, list_files, last_match
from gcd.obj import Object, get, keys, update
from gcd.hdl import Bus
from gcd.prs import elapsed
from gcd.run import cfg
from gcd.utl import fntime, get_name

def __dir__():
    return ("cmd", "flt", "thr", "upt")

def cmd(event):
    bot = Bus.by_orig(event.orig)
    if bot:
        c = sorted(keys(bot.cmds))
        if c:
            event.reply(",".join(c))

def flt(event):
    try:
        event.reply(str(Bus.objs[event.prs.index]))
        return
    except (TypeError, IndexError):
        pass
    event.reply(" | ".join([get_name(o) for o in Bus.objs]))

def thr(event):
    psformat = "%s %s"
    result = []
    for thr in sorted(threading.enumerate(), key=lambda x: x.getName()):
        if str(thr).startswith("<_"):
            continue
        o = Object()
        update(o, thr)
        if get(o, "sleep", None):
            up = o.sleep - int(time.time() - o.state.latest)
        else:
            up = int(time.time() - cfg.starttime)
        thrname = thr.getName()
        if not thrname:
            continue
        if thrname:
            result.append((up, thrname))
    res = []
    for up, txt in sorted(result, key=lambda x: x[0]):
        res.append("%s %s" % (txt, elapsed(up)))
    if res:
        event.reply(" | ".join(res))

def upt(event):
    return elapsed(time.time() - cfg.starttime)
