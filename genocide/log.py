# This file is placed in the Public Domain.


"log"


from hx.cmd import Commands
from hx.dbs import Class
from hx.obj import Object, save


def reg():
    Class.add(Log)
    Commands.add(log)


def rem():
    Class.remove(Log)
    Commands.remove(log)


class Log(Object):

    def __init__(self):
        super().__init__()
        self.txt = ""


def log(event):
    if not event.rest:
        event.reply("log <txt>")
        return
    o = Log()
    o.txt = event.rest
    save(o)
    event.reply("ok")
