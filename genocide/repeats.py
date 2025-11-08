# This file is placed in the Public Domain.


"non-blocking"


import logging
import queue
import threading
import time
import _thread


from typing import Any


class Thread(threading.Thread):

    def __init__(self, func, *args, daemon=True, **kwargs):
        super().__init__(None, self.run, None, (), daemon=daemon)
        self.name = kwargs.get("name", name(func))
        self.queue = queue.Queue()
        self.result = None
        self.starttime = time.time()
        self.stopped = threading.Event()
        self.queue.put((func, args))

    def __iter__(self):
        return self

    def __next__(self):
        yield from dir(self)

    def join(self, timeout=None) -> Any:
        super().join(timeout)
        return  self.result

    def run(self) -> None:
        func, args = self.queue.get()
        self.result = func(*args)


class Timy(threading.Timer):

    def __init__(self, sleep, func, *args, **kwargs):
        super().__init__(sleep, func)
        self.name = kwargs.get("name", name(func))
        self.sleep = sleep
        self.state = {}
        self.state["latest"] = time.time()
        self.state["starttime"] = time.time()
        self.starttime = time.time()


class Timed:

    def __init__(self, sleep, func, *args, thrname="", **kwargs):
        self.args = args
        self.func = func
        self.kwargs = kwargs
        self.sleep = sleep
        self.name = thrname or kwargs.get("name", name(func))
        self.target = time.time() + self.sleep
        self.timer = None

    def run(self) -> None:
        self.timer.latest = time.time()
        self.func(*self.args)

    def start(self) -> None:
        self.kwargs["name"] = self.name
        timer = Timy(self.sleep, self.run, *self.args, **self.kwargs)
        timer.start()
        self.timer = timer

    def stop(self) -> None:
        if self.timer:
            self.timer.cancel()


class Repeater(Timed):

    def run(self) -> None:
        launch(self.start)
        super().run()


def launch(func, *args, **kwargs) -> Thread:
    thread = Thread(func, *args, **kwargs)
    thread.start()
    return thread


def name(obj, short=False) -> str:
    typ = type(obj)
    res = ""
    if "__builtins__" in dir(typ):
        res = obj.__name__
    elif "__self__" in dir(obj):
        res = f"{obj.__self__.__class__.__name__}.{obj.__name__}"
    elif "__class__" in dir(obj) and "__name__" in dir(obj):
        res = f"{obj.__class__.__name__}.{obj.__name__}"
    elif "__class__" in dir(obj):
        res =  f"{obj.__class__.__module__}.{obj.__class__.__name__}"
    elif "__name__" in dir(obj):
        res = f"{obj.__class__.__name__}.{obj.__name__}"
    if short:
        res = res.split(".")[-1]
    return res


def threadhook(args) -> None:
    type, value, trace, thread = args
    exc = value.with_traceback(trace)
    if type not in (KeyboardInterrupt, EOFError):
        logging.exception(exc)
    _thread.interrupt_main()


LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning':logging. WARNING,
    'warn': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


class Logging:

    datefmt = "%H:%M:%S"
    format = "%(module).3s %(message)s"


class Format(logging.Formatter):

    def format(self, record):
        record.module = record.module.upper()
        return logging.Formatter.format(self, record)

def level(loglevel="debug"):
    if loglevel != "none":
        lvl = LEVELS.get(loglevel)
        if not lvl:
            return
        logger = logging.getLogger()
        for handler in logger.handlers:
            logger.removeHandler(handler)
        logger.setLevel(lvl)
        formatter = Format(Logging.format, datefmt=Logging.datefmt)
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)


def __dir__():
    return (
        'LEVELS',
        'Thread',
        'excepthook',
        'launch',
        'level',
        'name'
   )
