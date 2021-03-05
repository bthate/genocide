# This file is placed in the Public Domain.

"shell code"

# imports

import atexit
import ob
import readline
import sys

from . import update
from .hdl import Bus, Command, Bused, Cfg, Handler
from .prs import parse as p
from .thr import launch
from .trm import termreset, termsave

# classes

class Cfg(Cfg):

    pass

class Shell(Bused):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cfg = Cfg()

    def direct(self, txt):
        print(txt)

class Console(Shell):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handler = None
        self.add("cmd", cmd)

    def poll(self):
        self._connected.wait()
        c = Command(input("> "))
        c.orig = repr(self)
        c.origin = "root@console"
        if self.handler:
            self.handler.put(c)
        else:
            self.put(c)
        return c

    def start(self):
        launch(self.input)
        self._connected.set()

# functions

def exec(main):
    termsave()
    try:
        main()
    except KeyboardInterrupt:
        print("")
    except PermissionError as ex:
        print(str(ex))
    finally:
        termreset()

def op(ops):
    for opt in ops:
        if opt in ob.cfg.opts:
            return True
    return False

def parse():
    p(ob.cfg, " ".join(sys.argv[1:]))
    update(ob.cfg, ob.cfg.sets)
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
    cmds.extend(commands)
    readline.set_completer(complete)
    readline.parse_and_bind("tab: complete")
    atexit.register(lambda: readline.set_completer(None))

# commands

def cmd(event):
    b = Bus.by_orig(event.orig)
    event.reply(",".join(sorted(Handler.cmds)))

# runtime

cmds = []
