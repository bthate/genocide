# This file is placed in the Public Domain.

"log/todo"

# imports

import op

# classes

class Log(op.Object):

    def __init__(self):
        super().__init__()
        self.txt = ""

class Todo(op.Object):

    def __init__(self):
        super().__init__()
        self.txt = ""

# commands

def dne(event):
    if not event.res.args:
        return
    selector = {"txt": event.res.args[0]}
    for fn, o in op.dbs.find("gcd.ent.Todo", selector):
        o._deleted = True
        op.save(o)
        event.reply("ok")
        break

def log(event):
    if not event.res.rest:
        return
    l = Log()
    l.txt = event.res.rest
    op.save(l)
    event.reply("ok")

def tdo(event):
    if not event.res.rest:
        return
    o = Todo()
    o.txt = event.res.rest
    op.save(o)
    event.reply("ok")
