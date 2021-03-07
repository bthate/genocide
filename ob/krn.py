# This file is in the Public Domain.

"kern waardes"

import ob
import sys

from ob.bus import Bus
from ob.dbs import last

# classes

class Cfg(ob.Cfg):

    pass

class Shell(ob.hdl.Bused):

    def direct(self, txt):
        print(txt)

class Console(Shell):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handler = None

    def poll(self):
        self._connected.wait()
        c = ob.evt.Command(input("> "))
        c.orig = repr(self)
        c.origin = "root@console"
        if self.handler:
            self.handler.put(c)
        else:
            self.put(c)
        return c

    def start(self):
        ob.thr.launch(self.input)
        self._connected.set()

# functions

def op(ops):
    for opt in ops:
        if opt in cfg.opts:
            return True
    return False

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

def parse(name):
    ob.prs.parse(cfg, " ".join(sys.argv[1:]))
    ob.update(cfg, cfg.sets)
    cfg.name = name
    cfg.wd = cfg.wd or ob.e("~/.%s" % cfg.name)
    return cfg

# commands

def cmd(event):
    b = ob.bus.by_orig(event.orig)
    event.reply(",".join(sorted(b.handler.cmds or b.cmds)))

def krn(event):
    if not event.sets:
        event.reply(ob.format(cfg))
        return
    ob.edit(cfg, event.sets)
    ob.save(cfg)
    event.reply("ok")

def mod(event):
    event.reply(",".join(sorted({x.split(".")[-1] for x in ob.itr.find_modules(cfg.pkgs)})))

# runtime

cfg = Cfg()
cfg.pkgs = "ob,mod"
resume = ob.Object()
