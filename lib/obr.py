# This file is placed in the Public Domain.


"runtime"


from obb import Bus
from obe import Command, Parsed
from obh import Callbacks, Handler, Table, dispatch
from obj import Config, cdir, items, spl


class CLI(Handler):

    def __init__(self):
        Handler.__init__(self)
        Bus.add(self)

    def announce(self, txt):
        self.raw(txt)

    def cmd(self, txt):
        c = Command()
        c.channel = ""
        c.orig = repr(self)
        c.txt = txt
        self.handle(c)
        c.wait()

    def raw(self, txt):
        pass


class Console(CLI):

    def handle(self, e):
        Handler.handle(self, e)
        e.wait()

    def poll(self):
        e = Command()
        e.channel = ""
        e.cmd = ""
        e.txt = input("> ")
        e.orig = repr(self)
        if e.txt:
            e.cmd = e.txt.split()[0]
        return e


def boot(txt, pkgname="obm", mods=""):
    Callbacks.add("command", dispatch)
    cdir(Config.workdir)
    e = Parsed()
    e.parse(txt)
    for k, v in items(e):
        setattr(Config, k, v)
    for o in Config.opts:
        if o == "c":
            Config.console = True
        if o == "d":
            Config.daemon = True
        if o == "v":
            Config.verbose = True
    mns = mods or Config.sets.mods
    init(mns, pkgname, "reg")
    init(mns, pkgname, "init")
    return e


def init(mns, pn=None, cmds="init"):
    for mn in spl(mns):
        if pn:
            mn = pn + "." + mn
        mod = Table.get(mn)
        if not mod:
            continue
        for cmd in spl(cmds):
            c = getattr(mod, cmd, None)
            if not c:
                continue
            c()

def isopt(opts):
    for o in opts:
        if o in Config.opts:
            return True
