# This file is placed in the Public Domain.

"threads"

# imports

import ob
import queue
import threading

from . import Default, Object
from .utl import get_name

# classes

class Thr(threading.Thread):

    def __init__(self, func, *args, thrname="", daemon=True):
        super().__init__(None, self.run, thrname, (), {}, daemon=daemon)
        self._name = thrname or get_name(func)
        self._result = None
        self._queue = queue.Queue()
        self._queue.put_nowait((func, args))
        self.sleep = 0
        self.state = Object()

    def __iter__(self):
        return self

    def __next__(self):
        for k in dir(self):
            yield k

    def join(self, timeout=None):
        ""
        super().join(timeout)
        return self._result

    def run(self):
        ""
        func, args = self._queue.get_nowait()
        if args:
            try:
                target = Default(vars(args[0]))
                self._name = (target and target.txt and target.txt.split()[0]) or self._name
            except TypeError:
                pass
        self.setName(self._name)
        self._result = func(*args)

    def wait(self, timeout=None):
        super().join(timeout)
        return self._result

# functions

def launch(func, *args, **kwargs):
    name = kwargs.get("name", get_name(func))
    t = Thr(func, *args, thrname=name, daemon=True)
    t.start()
    if ob.cfg.verbose:
        print("launch %s" % t.getName())
    return t

# commands

def thr(event):
    import threading, time
    from . import Object, update
    psformat = "%s %s"
    result = []
    for thr in sorted(threading.enumerate(), key=lambda x: x.getName()):
        if str(thr).startswith("<_"):
            continue
        o = Object()
        update(o, thr)
        if getattr(o, "sleep", None):
            up = o.sleep - int(time.time() - o.state.latest)
        else:
            up = int(time.time() - starttime)
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
