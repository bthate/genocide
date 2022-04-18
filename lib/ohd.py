# This file is placed in the Public Domain.


"object handler"


import threading


from obj import Object
from obs import Bus
from ocb import Callback
from oqu import Queued
from oth import launch


def __dir__():
    return (
        "Handler",
    )


class Handler(Queued):

    errors = []

    def __init__(self):
        Queued.__init__(self)
        self.stopped = threading.Event()
        self.threaded = True

    def announce(self, txt):
        self.raw(txt)

    def handle(self, e):
        Callback.dispatch(e)

    def loop(self):
        while not self.stopped.isSet():
            self.handle(self.poll())

    def poll(self):
        return self.queue.get()

    def raw(self, txt):
        raise NotImplementedError

    def register(self, typ, cb):
        Callback.add(typ, cb)

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
