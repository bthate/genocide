# This file is placed in the Public Domain.


"fleet"


from hx.bus import Bus
from hx.cmd import Commands
from hx.thr import getname


def reg():
    Commands.add(flt)


def rem():
    Commands.remove(flt)


def flt(event):
    try:
        index = int(event.args[0])
        event.reply(Bus.objs[index])
        return
    except (KeyError, TypeError, IndexError, ValueError):
        pass
    event.reply(" | ".join([getname(o) for o in Bus.objs]))
