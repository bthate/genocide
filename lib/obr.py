# This file is placed in the Public Domain.


"scan modules"


import importlib
import inspect
import os
import sys
import termios
import traceback
import time


from obj import Config, cdir, items, spl
from obh import Callbacks, Event, Table


def boot(txt, pkgname="obm", mods=""):
    cdir(Config.workdir)
    e = Event()
    e.parse(txt)
    for k, v in items(e):
        setattr(Config, k, v)
    for o in Config.opts:
        if o == "d":
            Config.daemon = True
        if o == "v":
            Config.verbose = True
    init(mods, pkgname, "reg")
    init(mods, pkgname, "init")
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


def skip(fn):
    if not fn.endswith(".py"):
        return True
    if fn.endswith("~"):
        return True
    if fn.endswith("__.py"):
        return True
    return False


def wait():
    while 1:
        time.sleep(1.0)


def wrap(func):
    fd = sys.stdin.fileno()
    gotterm = True
    try:
        old = termios.tcgetattr(fd)
    except termios.error:
        gotterm = False
    try:
        func()
    except (EOFError, KeyboardInterrupt):
        print("")
    finally:
        if gotterm:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
