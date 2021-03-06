# This file is placed in the Public Domain.

"event handler"

# imports

import ob
import ob.prs
import os
import queue
import threading
import time
import _thread

# defines

loadlock = _thread.allocate_lock()

# classes

class Cfg(ob.Cfg):

    pass

class Handler(ob.Object):

    table = ob.Object()
    pnames = ob.Object()
    modnames = ob.Object()
    names = ob.ObjectList()

    def __init__(self, *args, **kwargs):
        super().__init__()
        self._connected = threading.Event()
        self.cbs = ob.Object()
        self.cfg = Cfg()
        self.cmds = ob.Object()
        self.queue = queue.Queue()
        self.started = []
        self.stopped = False
        if not args:
            from ob.tbl import tbl
        else:
            tbl = args[0]
        ob.update(Handler.names, tbl["names"])
        ob.update(Handler.modnames, tbl["modnames"])
        ob.update(Handler.pnames, tbl["pnames"])

    def add(self, cmd, func):
        self.cmds[cmd] = func
        Handler.modnames[cmd] = func.__module__
        
    def announce(self, txt):
        self.direct(txt)

    def cmd(self, txt):
        c = ob.evt.Command(txt)
        c.orig = repr(self)
        c.origin = "root@@console"
        cmd(self, c)
        c.wait()

    def direct(self, txt):
        pass

    def dispatch(self, event):
        if event.type and event.type in self.cbs:
            self.cbs[event.type](self, event)

    def get_cmd(self, cmd, autoload=False):
        if autoload and cmd not in self.cmds:
            mn = getattr(Handler.modnames, cmd, None)
            if mn:
                mod = self.load(mn)
        return getattr(self.cmds, cmd, None)

    def get_mod(self, mn):
        if mn in Handler.table:
            return Handler.table[mn]

    def get_names(self, nm):
        return getattr(Handler.names, nm, [nm,])

    def init(self, mns):
        thrs = []
        result = []
        for mn in ob.spl(mns):
            mn = getattr(Handler.pnames, mn, mn)
            mod = self.get_mod(mn)
            if mod and "init" in dir(mod):
                thrs.append(ob.thr.launch(mod.init, self))
        for thr in thrs:
            result.append(thr.join())
        return result

    def input(self):
        while not self.stopped:
            try:
                e = self.poll()
            except EOFError:
                break
            self.put(e)
            e.wait()

    @ob.utl.locked(loadlock)
    def load(self, mn):
        if not "." in mn:
            return None
        mod = ob.direct(mn)
        cmds = ob.itr.find_cmds(mod)
        ob.update(self.cmds, cmds)
        Handler.table[mn] = mod
        if "b" in ob.cfg.opts:
            print("load %s" % mn)
        return mod

    def load_mod(self, mns):
        mods = []
        if "all" in ob.spl(mns):
            mns = ",".join([x.split(".")[-1] for x in ob.itr.find_modules(ob.cfg.pkgs)])
        for mn in ob.spl(mns):
            mnn = getattr(Handler.pnames, mn, mn)
            try:
                mod = self.load(mnn)
                if mod:
                    mods.append(mod)
            except ModuleNotFoundError:
                pass
        if "d" in ob.cfg.opts and mods:
            print("load %s" % ",".join(sorted(mods)))
        return mods

    def handler(self):
        self.running = True
        while not self.stopped:
            e = self.queue.get()
            if not e:
                break
            if not e.orig:
                e.orig = repr(self)
            e.thrs.append(ob.thr.launch(self.dispatch, e))

    def put(self, e):
        self.queue.put_nowait(e)

    def register(self, name, callback):
        self.cbs[name] = callback

    def resume(self):
        last(self.cfg)

    def say(self, channel, txt):
        self.direct(txt)

    def scandir(self, path, name=""):
        if not os.path.exists(path):
            return
        if not name:
            name = path.split(os.sep)[-1]
        for mn in [x[:-3] for x in os.listdir(path)
                   if x and x.endswith(".py")
                   and not x.startswith("__")
                   and not x == "setup.py"]:
            fqn = "%s.%s" % (name, mn)
            if not has_mod(fqn):
                continue
            self.load(fqn)

    def start(self):
        ob.thr.launch(self.handler)

    def stop(self):
        self.stopped = True
        self.queue.put(None)

    def walk(self, nms="ob"):
        w = walk(nms)
        for c, mn in items(w.modnames):
            if has_mod(mn):
                self.load(mn)

    def wait(self):
        while not self.stopped:
            time.sleep(30.0)

class Core(Handler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register("cmd", cmd)

class Bused(Core):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ob.bus.Bus.add(self)

# functions

def cmd(handler, obj):
    obj.parse()
    res = None
    f = handler.get_cmd(obj.res.cmd, ob.cfg.autoload)
    if f:
        res = f(obj)
        obj.show()
    obj.ready()
    return res
