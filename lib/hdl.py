"handler (hdl)"

import importlib, inspect, os, queue, sys, threading, time

from obj import Default, Object, update
from prs import parse
from thr import launch, get_exception

debug = False

class Event(Default):

    "event class"

    __slots__ = ("prs", "src")

    def __init__(self):
        super().__init__()
        self.done = threading.Event()
        self.result = []
        
    def direct(self, txt):
        "send txt to console"
        print(txt)

    def parse(self, txt):
        "parse an event"
        self.prs = Default()
        parse(self.prs, txt)
        args = self.prs.txt.split()
        if args:
            self.cmd = args.pop(0)
        if args:
            self.args = args
            self.rest = " ".join(args)

    def ready(self):
        self.done.set()
        
    def reply(self, txt):
        "add txt to result"
        self.result.append(txt)

    def show(self):
        "display result"
        for txt in self.result:
            self.direct(txt)
        self.ready()
        
    def wait(self):
        self.done.wait()

class Handler(Object):

    "basic event handler"

    threaded = False

    def __init__(self):
        super().__init__()
        self.cbs = Object()
        self.queue = queue.Queue()
        self.stopped = False

    def clone(self, hdl):
        update(self.cbs, hdl.cbs)

    def cmd(self, txt):
        e = Event()
        e.txt = txt
        return self.dispatch(e)

    def dispatch(self, event):
        "run callbacks for event"
        if not event.src:
            event.src = self
        event.parse(event.txt)
        if event.cmd and event.cmd in self.cbs:
            self.cbs[event.cmd](event)
            event.show()
        event.ready()

    def handler(self):
        "handler loop"
        while not self.stopped:
            event = self.queue.get()
            if not event:
                break
            if self.threaded:
                event.thrs = []
                event.thrs.append(launch(self.dispatch, event, name=event.cmd))
                continue
            self.dispatch(event)

    def put(self, e):
        "put event on queue"
        self.queue.put_nowait(e)

    def register(self, name, callback):
        "register a callback"
        self.cbs[name] = callback

    def scan(self, mod):
        "scan for commands"
        for key, o in inspect.getmembers(mod, inspect.isfunction):
            if "event" in o.__code__.co_varnames:
                if o.__code__.co_argcount == 1:
                    self.register(key, o) 

    def scandir(self, path=None):
        "scan a modules directory"
        if not path:
            path = os.path.dirname(obj.__file__)
        sys.path.insert(0, path)
        for mn in [x[:-3] for x in os.listdir(path)
                          if x and x.endswith(".py")
                          and not x.startswith("__")
                          and not x == "setup.py"]:
            self.scan(direct(mn))

    def start(self):
        "start handler"
        launch(self.handler, name="Handler.handler")

    def stop(self):
        "stop handler"
        self.stopped = True
        self.queue.put(None)

    def walk(self, pkgname):
        "walk over packages and load their modules"
        mod = direct(pkgname)
        for name in [x[:-3] for x in os.listdir(mod.__path__[0])
                            if x.endswith(".py")]:
            self.scan(direct("%s.%s" % (pkgname, name)))
            
    def wait(self):
        if not self.stopped:
            time.sleep(30.0)

def direct(name):
    "load a module"
    return importlib.import_module(name, '')
