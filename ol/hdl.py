# GENOCIDE - the king of the netherlands commits genocide
#
# OTP-CR-117/19/001 otp.informationdesk@icc-cpi.int https://genocide.rtfd.io

import importlib
import ol
import pkgutil
import queue
import sys
import threading
import _thread

dispatchlock = _thread.allocate_lock()

class Handler(ol.Object):

    def __init__(self):
        super().__init__()
        self.queue = queue.Queue()
        self.stopped = False

    def dispatch(self, e):
        "overload this"

    def handler(self):
        while not self.stopped:
            event = self.queue.get()
            if not event:
                break
            if "orig" not in event:
                event.orig = repr(self)
            if event.txt:
                if self.cfg.nothread:
                    self.dispatch(event)
                else:
                    event.thrs.append(ol.tsk.launch(self.dispatch, event))
            else:
                event.ready.set()

    def put(self, e):
        self.queue.put_nowait(e)

    def start(self):
        ol.tsk.launch(self.handler)

    def stop(self):
        self.stopped = True
        self.queue.put(None)
