# This file is placed in the Public Domain.


"bus"


from op.obj import Object


def __dir__():
    return (
        "Bus",
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
            if o and "announce" in dir(o):
                o.announce(txt)

    @staticmethod
    def byorig(orig):
        for o in Bus.objs:
            if repr(o) == orig:
                return o

    @staticmethod
    def say(orig, channel, txt):
        o = Bus.byorig(orig)
        if o and "say" in dir(o):
            o.say(channel, txt)
