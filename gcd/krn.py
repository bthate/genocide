# This file is placed in the Public Domain.

"database,timer and tables"

import datetime
import os
import queue
import sys
import time
import threading
import types

from .dft import Default
from .obj import Object, cfg, spl, getname, gettype, search
from .prs import parse_txt
from .thr import launch

def __dir__():
    return ('Cfg', 'Kernel', 'Repeater', 'Timer', 'all', 'debug', 'deleted',
            'every', 'find', 'fns', 'fntime', 'hook', 'last', 'lastfn',
            'lastmatch', 'lasttype', 'listfiles')

all = "adm,cms,fnd,irc,krn,log,rss,tdo"

class ENOTYPE(Exception):

    pass

class Cfg(Default):

    pass

class Kernel(Object):

    cfg = Cfg()
    cmds = Object()
    fulls = Object()
    names = Default()
    modules = Object()
    table = Object()

    @staticmethod
    def addcmd(func):
        n = func.__name__
        Kernel.modules[n] = func.__module__
        Kernel.cmds[n] = func

    @staticmethod
    def addcls(cls):
        n = cls.__name__.lower()
        if n not in Kernel.names:
            Kernel.names[n] = []
        nn = "%s.%s" % (cls.__module__, cls.__name__)
        if nn not in Kernel.names[n]:
            Kernel.names[n].append(nn)

    @staticmethod
    def addmod(mod):
        n = mod.__spec__.name
        Kernel.fulls[n.split(".")[-1]] = n
        Kernel.table[n] = mod

    @staticmethod
    def boot(name, mods=None):
        if mods is None:
            mods = ""
        Kernel.cfg.name = name
        parse_txt(Kernel.cfg, " ".join(sys.argv[1:]))
        if Kernel.cfg.sets:
            Kernel.cfg.update(Kernel.cfg.sets)
        Kernel.cfg.save()
        Kernel.regs(mods or "irc,adm")

    @staticmethod
    def getcls(name):
        if "." in name:
            mn, clsn = name.rsplit(".", 1)
        else:
            raise ENOCLASS(fullname) from ex
        mod = Kernel.getmod(mn)
        return getattr(mod, clsn, None)

    @staticmethod
    def getcmd(c):
        return Kernel.cmds.get(c, None)

    @staticmethod
    def getfull(c):
        return Kernel.fulls.get(c, None)

    @staticmethod
    def getmod(mn):
        return Kernel.table.get(mn, None)

    @staticmethod
    def getnames(nm, dft=None):
        return Kernel.names.get(nm, dft)

    @staticmethod
    def getmodule(mn, dft):
        return Kernel.modules.get(mn ,dft)

    @staticmethod
    def init(mns):
        for mn in spl(mns):
            mnn = Kernel.getfull(mn)
            mod = Kernel.getmod(mnn)
            if "init" in dir(mod):
                launch(mod.init)

    @staticmethod
    def opts(ops):
        for opt in ops:
            if opt in Kernel.cfg.opts:
                return True
        return False

    @staticmethod
    def regs(mns):
        for mn in spl(mns):
            mnn = Kernel.getfull(mn)
            mod = Kernel.getmod(mnn)
            if "register" in dir(mod):
                mod.register(Kernel)

    @staticmethod
    def wait():
        while 1:
            time.sleep(5.0)

def kcmd(hdl, obj):
    obj.parse()
    f = Kernel.getcmd(obj.cmd)
    if f:
        f(obj)
        obj.show()
    sys.stdout.flush()
    obj.ready()

def hook(hfn):
    if hfn.count(os.sep) > 3:
        oname = hfn.split(os.sep)[-4:]
    else:
        oname = hfn.split(os.sep)
    cname = oname[0]
    fn = os.sep.join(oname)
    t = Kernel.getcls(cname)
    if not t:
        raise ENOTYPE(cname)
    if fn:
        o = t()
        o.load(fn)
        return o
    else:
        raise ENOTYPE(cname)
