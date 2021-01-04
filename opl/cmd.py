# OPL - object programming library (cmd.py)
#
# this file is placed in the public domain

"commands (cmd)"

# imports

import opl
import threading
import time

# defines

starttime = time.time()

def __dir__():
    return ("cfg", "cmd", "flt", "fnd", "log", "tdo", "thr", "dpl", "dne", "ftc", "rem", "rss", "ver")

# commands

# classes

class Log(opl.Object):

    "log items"

    def __init__(self):
        super().__init__()
        self.txt = ""

class Todo(opl.Object):

    "todo items"

    def __init__(self):
        super().__init__()
        self.txt = ""

# commands

def cmd(event):
    "list commands (cmd)"
    bot = opl.hdl.Bus.by_orig(event.orig)
    c = dir(opl.cmd)
    if bot:
        c.extend(bot.cmds)
        if c:
            event.reply(",".join(sorted(c)))

def dne(event):
    "flag as done (dne)"
    if not event.args:
        return
    selector = {"txt": event.args[0]}
    for fn, o in opl.dbs.find("opl.cmd.Todo", selector):
        o._deleted = True
        opl.save(o)
        event.reply("ok")
        break

def flt(event):
    "list of bots"
    try:
        event.reply(str(opl.hdl.Bus.objs[event.prs.index]))
        return
    except (TypeError, IndexError):
        pass
    event.reply(" | ".join([opl.get_name(o) for o in opl.hdl.Bus.objs]))

def fnd(event):
    "find objects (fnd)"
    if not event.args:
        fls = opl.dbs.list_files(opl.wd)
        if fls:
            event.reply(" | ".join([x.split(".")[-1].lower() for x in fls]))
        return
    nr = -1
    for otype in opl.get(opl.tbl.names, event.args[0], [event.args[0]]):
        for fn, o in opl.dbs.find(otype, event.prs.gets, event.prs.index, event.prs.timed):
            nr += 1
            txt = "%s %s" % (str(nr), opl.format(o, event.xargs or opl.keys(o), skip=event.prs.skip))
            if "t" in event.prs.opts:
                txt = txt + " %s" % (opl.prs.elapsed(time.time() - opl.utl.fntime(fn)))
            event.reply(txt)

def log(event):
    "log some text (log)"
    if not event.rest:
        return
    l = Log()
    l.txt = event.rest
    opl.save(l)
    event.reply("ok")

def tdo(event):
    "add a todo item (tdo)"
    if not event.rest:
        return
    o = Todo()
    o.txt = event.rest
    opl.save(o)
    event.reply("ok")

def thr(event):
    "list running threads (thr)"
    psformat = "%s %s"
    result = []
    for thr in sorted(threading.enumerate(), key=lambda x: x.getName()):
        if str(thr).startswith("<_"):
            continue
        o = opl.Object()
        opl.update(o, thr)
        if opl.get(o, "sleep", None):
            up = o.sleep - int(time.time() - o.state.latest)
        else:
            up = int(time.time() - opl.starttime)
        thrname = thr.getName()
        if not thrname:
            continue
        if thrname:
            result.append((up, thrname))
    res = []
    for up, txt in sorted(result, key=lambda x: x[0]):
        res.append("%s %s" % (txt, opl.prs.elapsed(up)))
    if res:
        event.reply(" | ".join(res))

def cfg(event):
    "configure irc (cfg)"
    c = opl.irc.Cfg()
    opl.dbs.last(c)
    if not event.prs.sets:
        return event.reply(opl.format(c, skip=["username", "realname"]))
    opl.update(c, event.prs.sets)
    opl.save(c)
    event.reply("ok")

def dpl(event):
    "set keys to display (dpl)"
    if len(event.args) < 2:
        return
    setter = {"display_list": event.args[1]}
    for fn, o in opl.dbs.last_match("opl.rss.Rss", {"rss": event.args[0]}):
        opl.edit(o, setter)
        opl.save(o)
        event.reply("ok")

def ftc(event):
    "run a fetch (ftc)"
    res = []
    thrs = []
    fetcher = opl.rss.Fetcher()
    fetcher.start(False)
    thrs = fetcher.run()
    for thr in thrs:
        res.append(thr.join() or 0)
    if res:
        event.reply("fetched %s" % ",".join([str(x) for x in res]))
        return

def rem(event):
    "remove a rss feed (rem)"
    if not event.args:
        return
    selector = {"rss": event.args[0]}
    nr = 0
    got = []
    for fn, o in opl.dbs.find("opl.rss.Rss", selector):
        nr += 1
        o._deleted = True
        got.append(o)
    for o in got:
        opl.save(o)
    event.reply("ok")

def rss(event):
    "add a rss feed (rss)"
    if not event.args:
        return
    url = event.args[0]
    res = list(opl.dbs.find("opl.rss.Rss", {"rss": url}))
    if res:
        return
    o = opl.rss.Rss()
    o.rss = event.args[0]
    opl.save(o)
    event.reply("ok")

def ver(event):
    "show version (ver)"
    event.reply("OPL %s - object programming library" % opl.__version__)
