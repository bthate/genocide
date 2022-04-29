# This file is placed in the Public Domain.


"handler"


import queue
import threading


from .obj import Object, get, register
from .prs import parse
from .thr import launch


def __dir__():
    return (
        'Bus',
        "Callbacks",
        "Commands",
        "Handler",
        "Table"
    )


class Bus(Object):

    objs = []

    @staticmethod
    def add(o):
        if repr(o) not in [repr(x) for x in Bus.objs]:
            Bus.objs.append(o)

    @staticmethod
    def announce(txt):
        for o in Bus.objs:
            o.announce(txt)

    @staticmethod
    def byorig(orig):
        for o in Bus.objs:
            if repr(o) == orig:
                return o

    @staticmethod
    def say(orig, channel, txt):
        o = Bus.byorig(orig)
        if o:
            o.say(channel, txt)


class Callbacks(Object):

    cbs = Object()
    errors = []
    threaded = True

    @staticmethod
    def add(name, cb):
        register(Callbacks.cbs, name, cb)

    @staticmethod
    def callback(e):
        f = Callbacks.get(e.type)
        if not f:
            e.ready()
            return
        try:
            f(e)
        except Exception as ex:
            Callbacks.errors.append(ex)
            e.exc = ex
            e.ready()

    @staticmethod
    def get(cmd):
        return get(Callbacks.cbs, cmd)


    @staticmethod
    def dispatch(e):
        if Callbacks.threaded:
            e.thrs.append(launch(Callbacks.callback, e, name=e.txt))
            return
        Callbacks.callback(e)



class Commands(Object):

    cmd = Object()

    @staticmethod
    def add(command):
        register(Commands.cmd, command.__name__, command)

    @staticmethod
    def get(command):
        f =  get(Commands.cmd, command)
        return f


class Table():

    mod = {}

    @staticmethod
    def add(o):
        Table.mod[o.__name__] = o

    @staticmethod
    def get(nm):
        return Table.mod.get(nm, None)


class Handler(Object):

    def __init__(self):
        Object.__init__(self)
        self.queue = queue.Queue()
        self.stopped = threading.Event()
        self.threaded = True

    def announce(self, txt):
        self.raw(txt)

    def handle(self, e):
        Callbacks.dispatch(e)

    def loop(self):
        while not self.stopped.isSet():
            self.handle(self.poll())

    def poll(self):
        return self.queue.get()

    def put(self, e):
        self.queue.put_nowait(e)

    def raw(self, txt):
        raise NotImplementedError

    def register(self, typ, cb):
        Callbacks.add(typ, cb)

    def restart(self):
        self.stop()
        self.start()

    def say(self, channel, txt):
        self.raw(txt)

    def start(self):
        Bus.add(self)
        self.stopped.clear()
        launch(self.loop)

    def stop(self):
        self.stopped.set()


def dispatch(e):
    parse(e, e.txt)
    f = Commands.get(e.cmd)
    if f:
        f(e)
        e.show()
    e.ready()

