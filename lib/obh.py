# This file is placed in the Public Domain.


"event handler"


import queue
import threading
import time
import types


from obj import Object
from obj import get, register


def __dir__():
    return (
        'Callbacks',
        'Commands',
        'Handler',
        'Repeater',
        'Table',
        'Thread',
        'Timer',
        'dispatch',
        "elapsed",
        'getname',
        'launch',
        'starttime',
    )


starttime = time.time()


class Callbacks(Object):

    cbs = Object()
    errors = []

    @staticmethod
    def add(name, cb):
        register(Callbacks.cbs, name, cb)

    @staticmethod
    def callback(e):
        f = Callbacks.get(e.type)
        if not f:
            e.ready()
            return
        f(e)

    @staticmethod
    def get(cmd):
        return get(Callbacks.cbs, cmd)

    @staticmethod
    def dispatch(e):
        Callbacks.callback(e)


class Commands(Object):

    cmd = Object()

    @staticmethod
    def add(cmd):
        register(Commands.cmd, cmd.__name__, cmd)

    @staticmethod
    def get(cmd):
        return get(Commands.cmd, cmd)


    @staticmethod
    def remove(cmd):
        del Commands.cmd[cmd]


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
        self.cache = Object()
        self.queue = queue.Queue()
        self.stopped = threading.Event()
        self.threaded = False

    def announce(self, txt):
        self.raw(txt)

    def forever(self):
        while 1:
            time.sleep(1.0)

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
        pass

    def register(self, typ, cb):
        Callbacks.add(typ, cb)

    def restart(self):
        self.stop()
        self.start()

    def say(self, channel, txt):
        self.raw(txt)

    def start(self):
        self.stopped.clear()
        launch(self.loop)

    def stop(self):
        self.stopped.set()


class Thread(threading.Thread):

    def __init__(self, func, name, *args, daemon=True):
        super().__init__(None, self.run, name, (), {}, daemon=daemon)
        self._exc = None
        self._evt = None
        self.name = name
        self.queue = queue.Queue()
        self.queue.put_nowait((func, args))
        self._result = None

    def __iter__(self):
        return self

    def __next__(self):
        for k in dir(self):
            yield k

    def join(self, timeout=None):
        super().join(timeout)
        return self._result

    def run(self):
        func, args = self.queue.get()
        if args:
            self._evt = args[0]
        self.setName(self.name)
        self._result = func(*args)
        return self._result


class Timer(Object):

    def __init__(self, sleep, func, *args, name=None):
        super().__init__()
        self.args = args
        self.func = func
        self.sleep = sleep
        self.name = name or ""
        self.state = Object()
        self.timer = None

    def run(self):
        self.state.latest = time.time()
        launch(self.func, *self.args)

    def start(self):
        if not self.name:
            self.name = getname(self.func)
        timer = threading.Timer(self.sleep, self.run)
        timer.setName(self.name)
        timer.setDaemon(True)
        timer.sleep = self.sleep
        timer.state = self.state
        timer.state.starttime = time.time()
        timer.state.latest = time.time()
        timer.func = self.func
        timer.start()
        self.timer = timer
        return timer

    def stop(self):
        if self.timer:
            self.timer.cancel()


class Repeater(Timer):

    def run(self):
        thr = launch(self.start)
        super().run()
        return thr


def dispatch(e):
    e.parse()
    f = Commands.get(e.cmd)
    if f:
        f(e)
        e.show()
    e.ready()


def elapsed(seconds, short=True):
    txt = ""
    nsec = float(seconds)
    year = 365*24*60*60
    week = 7*24*60*60
    nday = 24*60*60
    hour = 60*60
    minute = 60
    years = int(nsec/year)
    nsec -= years*year
    weeks = int(nsec/week)
    nsec -= weeks*week
    nrdays = int(nsec/nday)
    nsec -= nrdays*nday
    hours = int(nsec/hour)
    nsec -= hours*hour
    minutes = int(nsec/minute)
    sec = nsec - minutes*minute
    if years:
        txt += "%sy" % years
    if weeks:
        nrdays += weeks * 7
    if nrdays:
        txt += "%sd" % nrdays
    if years and short and txt:
        return txt
    if hours:
        txt += "%sh" % hours
    if nrdays and short and txt:
        return txt
    if minutes:
        txt += "%sm" % minutes
    if hours and short and txt:
        return txt
    if sec == 0:
        txt += "0s"
    else:
        txt += "%ss" % int(sec)
    txt = txt.strip()
    return txt


def getname(o):
    t = type(o)
    if isinstance(t, types.ModuleType):
        return o.__name__
    if "__self__" in dir(o):
        return "%s.%s" % (o.__self__.__class__.__name__, o.__name__)
    if "__class__" in dir(o) and "__name__" in dir(o):
        return "%s.%s" % (o.__class__.__name__, o.__name__)
    if "__class__" in dir(o):
        return o.__class__.__name__
    if "__name__" in dir(o):
        return o.__name__
    return None


def launch(func, *args, **kwargs):
    name = kwargs.get("name", getname(func))
    t = Thread(func, name, *args)
    t.start()
    return t
