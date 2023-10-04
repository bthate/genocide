#!/usr/bin/env python3
# This file is placed in the Public Domain.
#
# pylint: disable=C0412,C0115,C0116,W0212,R0903,C0207,C0413,W0611
# pylint: disable=C0411,E0402,E0611

"runtime"


import os
import sys
import termios
import traceback


from .runtime import Cfg, Client, Errors, Event, command, mods
from .runtime import output, parse, scan
from .storage import Storage


from . import  modules


ALL = ",".join(mods(modules.__path__[0]))


NAME = __file__.split(os.sep)[-1]
if ".py" in NAME:
    NAME = __file__.split(os.sep)[-2]


VERSION = "150"


Storage.workdir = os.path.expanduser(f"~/.{NAME}")


def cprint(txt):
    print(txt)
    sys.stdout.flush()


output = cprint


class CLI(Client):

    def raw(self, txt):
        print(txt)
        sys.stdout.flush()


class Console(CLI):

    def dispatch(self, evt):
        command(evt)
        evt.wait()

    def poll(self) -> Event:
        return self.event(input("> "))


def daemon():
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    os.umask(0)
    with open('/dev/null', 'r', encoding="utf-8") as sis:
        os.dup2(sis.fileno(), sys.stdin.fileno())
    with open('/dev/null', 'a+', encoding="utf-8") as sos:
        os.dup2(sos.fileno(), sys.stdout.fileno())
    with open('/dev/null', 'a+', encoding="utf-8") as ses:
        os.dup2(ses.fileno(), sys.stderr.fileno())


def wrap(func) -> None:
    old = None
    try:
        old = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (EOFError, KeyboardInterrupt):
        cprint("")
        sys.stdout.flush()
    finally:
        if old:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old)
    Errors.show()


def ver(event):
    event.reply(f"{NAME.upper()} {VERSION}")


def main():
    parse(Cfg, " ".join(sys.argv[1:]))
    if "x" not in Cfg.opts:
        Cfg.mod = Cfg.mod or ALL
    if "d" in Cfg.opts:
        daemon()
    if "d" in Cfg.opts:
        cli = CLI()
        scan(modules, Cfg.mod, True)
        cli.forever()
    elif "c" in Cfg.opts:
        if 'v' in Cfg.opts:
            print(f"{NAME.upper()} {VERSION} {Cfg.opts.upper()} {Cfg.mod.upper()}")
        scan(modules, Cfg.mod, "i" in Cfg.opts, True)
        csl = Console()
        csl.add(ver)
        csl.start()
        csl.forever()
    else:
        cli = CLI()
        cli.add(ver)
        scan(modules, Cfg.mod)
        evt = cli.event(Cfg.otxt)
        command(evt)
        evt.wait()


if __name__ == "__main__":
    wrap(main)
