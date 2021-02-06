# This file is in the Public Domain.
 
from gcd.obj import Object, format, get, keys
from gcd.dbs import find, list_files
from gcd.hdl import Bus
from gcd.prs import elapsed
from gcd.run import cfg
from gcd.utl import fntime, get_names, time

def __dir__():
    return ("fnd",)

def fnd(event):
    if not event.args:
        fls = list_files(cfg.wd)
        if fls:
            event.reply("|".join([x.split(".")[-1].lower() for x in fls]))
        return
    name = event.args[0]
    bot = Bus.by_orig(event.orig)
    t = get(bot.names, name, [name])
    nr = -1
    for otype in t:
        for fn, o in find(otype, event.prs.gets, event.prs.index, event.prs.timed):
            nr += 1
            txt = "%s %s" % (str(nr), format(o, event.xargs or keys(o), skip=event.prs.skip))
            if "t" in event.prs.opts:
                txt = txt + " %s" % (elapsed(time.time() - fntime(fn)))
            event.reply(txt)
