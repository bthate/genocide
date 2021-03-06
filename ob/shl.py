# This file is placed in the Public Domain.

"shell code"

# imports

import atexit
import ob
import readline
import sys

# classes

class Cfg(ob.Cfg):

    pass

class Shell(ob.hdl.Bused):

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
    ob.trm.termsave()
    try:
        main()
    except KeyboardInterrupt:
        print("")
    except PermissionError as ex:
        print(str(ex))
    finally:
        ob.trm.termreset()

def op(ops):
    for opt in ops:
        if opt in ob.cfg.opts:
            return True
    return False

def parse():
    ob.prs.parse(ob.cfg, " ".join(sys.argv[1:]))
    ob.update(ob.cfg, ob.cfg.sets)
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

# runtime

cmds = []
