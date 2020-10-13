# OLIB - object library
#
#

import ol

classes = ol.Object()
mods = ol.Object()
funcs = ol.Object()
names = ol.Object()

ol.update(classes, {"Bus": ["ol.bus"], "Cfg": ["bot.irc"], "Console": ["ol.csl"], "DCC": ["bot.irc"], "Email": ["mymod.mbx"], "Event": ["bot.irc"], "Feed": ["bmod.rss"], "Fetcher": ["bmod.rss"], "Getter": ["ol.prs"], "Handler": ["ol.hdl"], "IRC": ["bot.irc"], "Kernel": ["ol.krn"], "Loader": ["ol.ldr"], "Log": ["bmod.ent"], "Option": ["ol.prs"], "Repeater": ["ol.tms"], "Rss": ["bmod.rss"], "Seen": ["bmod.rss"], "Setter": ["ol.prs"], "Skip": ["ol.prs"], "Timed": ["ol.prs"], "Timer": ["ol.tms"], "Todo": ["bmod.ent"], "Token": ["ol.prs"], "UDP": ["bmod.udp"], "User": ["bot.irc"], "Users": ["bot.irc"]})

ol.update(mods, {"cfg": "bmod.cfg", "cmd": "bmod.cmd", "cor": "mymod.mbx", "dne": "bmod.ent", "dpl": "bmod.rss", "edt": "mymod.edt", "eml": "mymod.mbx", "fed": "bmod.rss", "fnd": "bmod.fnd", "ftc": "bmod.rss", "krn": "mymod.dbg", "log": "bmod.ent", "mbx": "mymod.mbx", "mds": "mymod.dbg", "req": "genocide.request", "rm": "bmod.rss", "rss": "bmod.rss", "sts": "genocide.stats", "tbl": "mymod.dbg", "tdo": "bmod.ent", "trt": "genocide.torture", "tsk": "bmod.cmd", "upt": "bmod.cmd", "ver": "bmod.cmd", "wsd": "genocide.wisdom"})

ol.update(funcs, {"cfg": "bmod.cfg.cfg", "cmd": "bmod.cmd.cmd", "cor": "mymod.mbx.cor", "dne": "bmod.ent.dne", "dpl": "bmod.rss.dpl", "edt": "mymod.edt.edt", "eml": "mymod.mbx.eml", "fed": "bmod.rss.fed", "fnd": "bmod.fnd.fnd", "ftc": "bmod.rss.ftc", "krn": "mymod.dbg.krn", "log": "bmod.ent.log", "mbx": "mymod.mbx.mbx", "mds": "mymod.dbg.mds", "req": "genocide.request.req", "rm": "bmod.rss.rm", "rss": "bmod.rss.rss", "sts": "genocide.stats.sts", "tbl": "mymod.dbg.tbl", "tdo": "bmod.ent.tdo", "trt": "genocide.torture.trt", "tsk": "bmod.cmd.tsk", "upt": "bmod.cmd.upt", "ver": "bmod.cmd.ver", "wsd": "genocide.wisdom.wsd"})

ol.update(names, {"bus": ["ol.bus.Bus"], "cfg": ["bot.irc.Cfg"], "console": ["ol.csl.Console"], "dcc": ["bot.irc.DCC"], "email": ["mymod.mbx.Email"], "event": ["bot.irc.Event"], "feed": ["bmod.rss.Feed"], "fetcher": ["bmod.rss.Fetcher"], "getter": ["ol.prs.Getter"], "handler": ["ol.hdl.Handler"], "irc": ["bot.irc.IRC"], "kernel": ["ol.krn.Kernel"], "loader": ["ol.ldr.Loader"], "log": ["bmod.ent.Log"], "option": ["ol.prs.Option"], "repeater": ["ol.tms.Repeater"], "rss": ["bmod.rss.Rss"], "seen": ["bmod.rss.Seen"], "setter": ["ol.prs.Setter"], "skip": ["ol.prs.Skip"], "timed": ["ol.prs.Timed"], "timer": ["ol.tms.Timer"], "todo": ["bmod.ent.Todo"], "token": ["ol.prs.Token"], "udp": ["bmod.udp.UDP"], "user": ["bot.irc.User"], "users": ["bot.irc.Users"]})
