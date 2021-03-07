# This file is in the Public Domain.

"events"

# imports

import ob
import threading

# classes

class Event(ob.Default):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.channel = ""
        self.done = threading.Event()
        self.orig = None
        self.result = []
        self.thrs = []
        self.type = "event"
        self.txt = ""
        if args:
            self.txt = args[0]

    def direct(self, txt):
        ob.bus.Bus.say(self.orig, self.channel, txt)

    def parse(self):
        ob.prs.parse(self, self.txt)

    def ready(self):
        self.done.set()

    def reply(self, txt):
        self.result.append(txt)

    def show(self):
        for txt in self.result:
            self.direct(txt)

    def wait(self, timeout=1.0):
        self.done.wait(timeout)
        for thr in self.thrs:
            thr.join()

class Command(Event):

    def __init__(self, txt="", **kwargs):
        super().__init__(**kwargs)
        self.type = "cmd"
        self.txt = txt.rstrip()
