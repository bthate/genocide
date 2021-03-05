# This file is placed in the Public Domain.

"shell code"

# imports

import atexit
import ob
import readline
import sys

from .hdl import Bused, Cfg
from .prs import parse as p

# defines

def init(h):
    shl = Shell()
    shl.clone(h)
    shl.start()
    return shl

# classes

class Cfg(Cfg):

    pass

class Shell(Bused):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cfg = Cfg()

    def direct(self, txt):
        pass

# functions

def op(ops):
    for opt in ops:
        if opt in ob.cfg.opts:
            return True
    return False

def parse():
    p(ob.cfg, " ".join(sys.argv[1:]))
    return ob.cfg

def complete(text, state):
    matches = []
    if text:
        matches = [s for s in cmds if s and s.startswith(text)]
    else:
        matches = cmds[:]
    try:
        return matches[state]
    except IndexError:
        return None

def setcompleter(commands):
    "set the completer"
    cmds.extend(commands)
    readline.set_completer(complete)
    readline.parse_and_bind("tab: complete")
    atexit.register(lambda: readline.set_completer(None))


# runtime

cmds = []
