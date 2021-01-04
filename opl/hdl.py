# OPL - object programming library (hdl.py)
#
# this file is placed in the public domain

"handler (hdl)"

# imports

import inspect
import importlib
import importlib.util
import opl
import opl.cmd
import os
import queue
import sys
import threading
import time

# defines

def __dir__():
    return ("Bus", "Command", "Event", "Handler", "cmd")

# classes

class Bus(opl.Object):

    "registered recipient event handler"

    objs = []

    def __call__(self, *args, **kwargs):
        return Bus.objs

    def __iter__(self):
        return iter(Bus.objs)

    @staticmethod
    def add(obj):
        "listener"
        Bus.objs.append(obj)

    @staticmethod
    def announce(txt, skip=None):
        "all listeners"
        for h in Bus.objs:
            if skip is not None and isinstance(h, skip):
                continue
            if "announce" in dir(h):
                h.announce(txt)

    @staticmethod
    def by_orig(orig):
        "listener"
        for o in Bus.objs:
            if repr(o) == orig:
                return o

    @staticmethod
    def say(orig, channel, txt):
        "say to specific listener"
        for o in Bus.objs:
            if repr(o) == orig:
                o.say(channel, str(txt))

class Event(opl.Default):

    "event class"

    __slots__ = ("prs", "src")

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.channel = ""
        self.done = threading.Event()
        self.orig = None
        self.result = []
        self.thrs = []
        self.type = "event"

    def direct(self, txt):
        "send txt to console - overload this"
        Bus.say(self.orig, self.channel, txt)

    def parse(self):
        "parse an event"
        self.prs = opl.Default()
        opl.prs.parse(self.prs, self.otxt or self.txt)
        args = self.prs.txt.split()
        if args:
            self.cmd = args.pop(0)
        if args:
            self.args = list(args)
            self.rest = " ".join(self.args)
            self.otype = args.pop(0)
        if args:
            self.xargs = args

    def ready(self):
        "event is handled"
        self.done.set()

    def reply(self, txt):
        "add txt to result"
        self.result.append(txt)

    def show(self):
        "display result"
        for txt in self.result:
            self.direct(txt)

    def wait(self):
        "wait"
        self.done.wait()
        for thr in self.thrs:
            thr.join()

class Command(Event):

    "based on txt"

    def __init__(self, txt, **kwargs):
        super().__init__([], **kwargs)
        self.type = "cmd"
        if txt:
            self.txt = txt

class Handler(opl.Object):

    "event handler"

    threaded = False

    def __init__(self):
        super().__init__()
        self.cbs = opl.Object()
        self.cmds = opl.Object()
        self.modnames = opl.Object()
        self.names = opl.Ol()
        self.queue = queue.Queue()
        self.stopped = False
        Bus.add(self)

    def clone(self, hdl):
        "copy callbacks"
        opl.update(self.cmds, hdl.cmds)
        opl.update(self.cbs, hdl.cbs)
        opl.update(self.modnames, hdl.modnames)
        opl.update(self.names, hdl.names)

    def cmd(self, txt):
        "execute command"
        self.register("cmd", cmd)
        c = Command(txt)
        c.orig = repr(self)
        cmd(self, c)
        c.wait()

    def direct(self, txt):
        "outputs text, overload this"

    def dispatch(self, event):
        "run callbacks for event"
        if event.type and event.type in self.cbs:
            self.cbs[event.type](self, event)

    def fromdir(self, path, name="opl"):
        "scan a modules directory"
        if not path:
            return
        for mn in [x[:-3] for x in os.listdir(path)
                   if x and x.endswith(".py")
                   and not x.startswith("__")
                   and not x == "setup.py"]:
            self.intro(opl.utl.direct("%s.%s" % (name, mn)))

    def init(self, mns, name="opl"):
        "call init() of modules"
        thrs = []
        for mn in opl.utl.spl(mns):
            try:
                spec = importlib.util.find_spec("%s.%s" % (name, mn))
            except ModuleNotFoundError:
                continue
            if spec:
                mod = self.load("%s.%s" % (name, mn))
                self.intro(mod)
                func = getattr(mod, "init", None)
                if func:
                    thrs.append(func(self))
        return thrs

    def intro(self, mod):
        "introspect a module"
        for key, o in inspect.getmembers(mod, inspect.isfunction):
            if o.__code__.co_argcount == 1:
                if o.__code__.co_varnames[0] == "obj":
                    self.register(key, o)
                elif o.__code__.co_varnames[0] == "event":
                    self.cmds[key] = o
                self.modnames[key] = o.__module__
        for _key, o in inspect.getmembers(mod, inspect.isclass):
            if issubclass(o, opl.Object):
                t = "%s.%s" % (o.__module__, o.__name__)
                self.names.append(o.__name__.lower(), t)
        return mod

    def load(self, mn):
        "load from modulename"
        if mn in sys.modules:
            mod = sys.modules[mn]
        else:
            mod = opl.utl.direct(mn)
        self.intro(mod)
        return mod

    def handler(self):
        "handler loop"
        self.running = True
        while not self.stopped:
            e = self.queue.get()
            if not e:
                break
            if not e.orig:
                e.orig = repr(self)
            e.thrs.append(opl.thr.launch(self.dispatch, e))

    def put(self, e):
        "put event on queue"
        self.queue.put_nowait(e)

    def register(self, name, callback):
        "register a callback"
        self.cbs[name] = callback

    def say(self, channel, txt):
        "forward to direct"
        self.direct(txt)

    def start(self):
        "start handler"
        opl.thr.launch(self.handler)

    def stop(self):
        "stop handler"
        self.stopped = True
        self.queue.put(None)

    def walk(self, pkgnames, name=""):
        "walk over packages and load their modules"
        if not name:
            name = list(opl.utl.spl(pkgnames))[0]
        for pn in opl.utl.spl(pkgnames):
            mod = self.load(pn)
            self.fromdir(mod.__path__[0], name)

    def wait(self):
        "wait for handler stopped status"
        if not self.stopped:
            while 1:
                time.sleep(30.0)

# functions

def cmd(handler, obj):
    "dispatch to command"
    obj.parse()
    f = getattr(opl.cmd, obj.cmd, None)
    if not f:
        f = opl.get(handler.cmds, obj.cmd, None)
    res = None
    if f:
        res = f(obj)
        obj.show()
    obj.ready()
    return res

# runtime

md = ""
