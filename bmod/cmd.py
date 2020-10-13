# BOTLIB - the bot library !
#
#

__version__ = 1

import ol
import threading
import time

k = ol.krn.get_kernel()

def cmd(event):
    c = sorted(ol.keys(ol.tbl.mods))
    if c:
        event.reply(",".join(c))

def tsk(event):
    psformat = "%s %s"
    result = []
    for thr in sorted(threading.enumerate(), key=lambda x: x.getName()):
        if str(thr).startswith("<_"):
            continue
        d = vars(thr)
        o = ol.Object()
        ol.update(o, d)
        if ol.get(o, "sleep", None):
            up = o.sleep - int(time.time() - o.state.latest)
        else:
            up = int(time.time() - ol.krn.starttime)
        thrname = thr.getName()
        result.append((up, psformat % (thrname, ol.tms.elapsed(up))))
    res = []
    for up, txt in sorted(result, key=lambda x: x[0]):
        res.append(txt)
    event.reply(" | ".join(res))

def upt(event):
    event.reply(ol.tms.elapsed(time.time() - ol.krn.starttime))

def ver(event):
    import genocide
    event.reply("GENOCLAIN %s | BOTLIB %s | OLIB %s | %s" % (genocide.__version__, __version__, ol.__version__, genocide.__txt2__))
