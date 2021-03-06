# This file is placed in the Public Domain.

"event handler"

# imports

import ob

# classes

class Bus(ob.Object):

    objs = []

    def __call__(self, *args, **kwargs):
        return Bus.objs

    def __iter__(self):
        return iter(Bus.objs)

    @staticmethod
    def add(obj):
        Bus.objs.append(obj)

    @staticmethod
    def announce(txt, skip=None):
        for h in Bus.objs:
            if skip is not None and isinstance(h, skip):
                continue
            if "announce" in dir(h):
                h.announce(txt)

    @staticmethod
    def by_orig(orig):
        for o in Bus.objs:
            if repr(o) == orig:
                return o
    @staticmethod
    def resume():
        for o in Bus.objs:
            o.resume()

    @staticmethod
    def save():
        for o in Bus.objs:
            save(o)

    @staticmethod
    def say(orig, channel, txt):
        for o in Bus.objs:
            if repr(o) == orig:
                o.say(channel, str(txt))

# commands

def flt(event):
    try:
        event.reply(str(Bus.objs[event.index]))
        return
    except (TypeError, IndexError):
        pass
    event.reply(" | ".join([ob.get_name(o) for o in Bus.objs]))
