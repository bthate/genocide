# This file is placed in the Public Domain.

"find objects"

# imports

import ob

# commands

def fnd(event):
    if not event.res.args:
        fls = ob.dbs.list_files(cfg.wd)
        if fls:
            event.reply("|".join([x.split(".")[-1].lower() for x in fls]))
        return
    name = event.res.args[0]
    bot = ob.bus.Bus.by_orig(event.orig)
    t = bot.get_names(name)
    nr = -1
    for otype in t:
        for fn, o in ob.dbs.find(otype, event.gets, event.res.index, event.res.timed):
            nr += 1
            txt = "%s %s" % (str(nr), ob.format(o, ob.keys(o), skip=event.skip))
            if "t" in event.opts:
                txt = txt + " %s" % (elapsed(time.time() - ob.utl.fntime(fn)))
            event.reply(txt)
