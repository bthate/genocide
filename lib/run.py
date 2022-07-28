# This file is placed in the Public Domain.


"scan modules"


import importlib
import inspect
import os
import sys
import termios
import time


from obj import Config, cdir, items, spl
from hdl import Callbacks, Event, Table


def boot(txt):
    e = Event()
    e.parse(txt)
    for k, v in items(e):
        setattr(Config, k, v)
    for o in Config.opts:
        if o == "-v":
           Config.verbose = True 
    return e


def init(mns, pn=None, cmds="init"):
    for mn in spl(mns):
        if pn:
            mn = pn + "." + mn
        mod = importlib.import_module(mn)
        if not mod:
            continue
        for cmd in spl(cmds):
            c = getattr(mod, cmd, None)
            if not c:
                continue
            try:
                c()
            except Exception as ex:
                Callbacks.errors.append(ex)


def introspect(mod):
    for k, o in inspect.getmembers(mod, inspect.isfunction):
        if "event" in o.__code__.co_varnames[:o.__code__.co_argcount]:
            Commands.cmd[k] = o
    for k, clz in inspect.getmembers(mod, inspect.isclass):
        Class.add(clz)


def isopt(opts):
    for o in opts:
        if o in Config.opts:
            return True

def scan(dn, intro=False):
    mods = []
    for mod in scandir(dn):
        if intro:
            introspect(mod)
        Table.add(mod)
        mods.append(mod)
    return mods


def scandir(dn):
    dns = []
    if "." in dn:
        pn = dn
    else:
        pn = dn.split(os.sep)[-1]
    if os.path.exists(dn):
        dns.append(dn)
        sys.path.insert(0, dn)
    if not dns:
        try:
            pkg = importlib.import_module(dn)
            if pkg:
                if pkg.__file__:
                    dns.append(os.path.dirname(pkg.__file__))
                else:
                    dns.extend(pkg.__path__)
        except Exception as ex:
            dns = [dn,]
            Callbacks.errors.append(ex)
    result = []
    for dnn in dns:
        if not os.path.exists(dnn):
            continue
        for mn in os.listdir(dnn):
            if skip(mn):
                continue
            mn = mn[:-3]
            try:
                result.append(importlib.import_module(mn, pn))
            except Exception as ex:
                Callbacks.errors.append(ex)
    return result


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
        for err in Callbacks.errors:
            traceback.print_exception(type(err), err, err.__traceback__)


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
            for err in Callbacks.errors:
                traceback.print_exception(type(err), err, err.__traceback__)