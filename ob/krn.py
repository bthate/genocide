# This file is in the Public Domain.

"kern waardes"

import ob
import readline
import sys

from ob.bus import Bus
from ob.dbs import last

# classes

class Cfg(ob.Cfg):

    pass

class Shell(ob.hdl.Bused):

    def direct(self, txt):
        if not self.stopped:
            print(txt)

class Console(Shell):

    def poll(self):
        self._connected.wait()
        c = ob.evt.Command(input("> "))
        c.orig = repr(self)
        c.origin = "root@console"
        return c

    def start(self):
        super().start()
        ob.thr.launch(self.input)
        ob.trm.setcompleter(self.cmds)
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

def parse(name, pkgs="ob,mod"):
    ob.prs.parse(cfg, " ".join(sys.argv[1:]))
    ob.update(cfg, cfg.sets)
    cfg.name = name
    ob.wd = cfg.wd = cfg.wd or ob.wd or ob.e("~/.%s" % cfg.name)
    cfg.pkgs = pkgs
    return cfg

# commands

def cmd(event):
    b = ob.bus.by_orig(event.orig)
    event.reply(",".join(sorted(b.cmds)))

def krn(event):
    if not event.sets:
        event.reply(ob.format(cfg, skip=["opts", "sets", "old", "res"]))
        return
    ob.edit(cfg, event.sets)
    ob.save(cfg)
    event.reply("ok")

def load(event):
    b = ob.bus.by_orig(event.orig)
    if event.res.rest:
        b.load_mod(event.res.rest)
        event.reply("ok")    

def mod(event):
    event.reply(",".join(sorted({x.split(".")[-1] for x in ob.itr.find_modules(cfg.pkgs)})))

# runtime

cfg = Cfg()
resume = ob.Object()
