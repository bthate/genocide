# This file is placed in the Public Domain.


"client"


from op.obj import Object


class Client(Object):

    def __init__(self):
        Object.__init__(self)
        self.orig = repr(self)

    def announce(self, txt):
        self.raw(txt)

    def raw(self, txt):
        pass

    def say(self, channel, txt):
        self.raw(txt)
