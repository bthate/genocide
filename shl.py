# This file is placed in the Public Domain.
# pylint: disable=C,I,R,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


import readline
import sys
import termios
import traceback


readline.redisplay()


from genocide.clients import Client
from genocide.command import command
from genocide.errored import Errors
from genocide.loggers import Logging
from genocide.message import parse
from genocide.objects import update
from genocide.persist import Persist
from genocide.scanner import importer, scandir, scanpkg, threader
from genocide.runtime import Cfg


import genocide.modules


def cprint(txt):
    if "v" in Cfg.opts:
        print(txt)
        sys.stdout.flush()


Logging.raw = cprint


class CLI(Client):

    def announce(self, txt):
        pass

    def raw(self, txt):
        print(txt)
        sys.stdout.flush()


def main():
    cfg = parse(' '.join(sys.argv[1:]))
    update(Cfg, cfg)
    scanpkg(genocide.modules, importer, Cfg.sets.mod or Cfg.mod, threader)
    scandir(Persist.moddir(), importer, Cfg.sets.mod or Cfg.mod, threader)
    scandir("mod", importer, Cfg.sets.mod or Cfg.mod, threader)
    cli = CLI()
    command(cli, Cfg.otxt)


def waiter():
    got = []
    for ex in Errors.errors:
        traceback.print_exception(type(ex), ex, ex.__traceback__)
        got.append(ex)
    for exc in got:
        Errors.errors.remove(exc)


def wrap(func):
    fds = sys.stdin.fileno()
    gotterm = True
    try:
        old = termios.tcgetattr(fds)
    except termios.error:
        gotterm = False
    try:
        func()
    except (EOFError, KeyboardInterrupt):
        print("")
    finally:
        if gotterm:
            termios.tcsetattr(fds, termios.TCSADRAIN, old)
        waiter()


if __name__ == "__main__":
    wrap(main)
