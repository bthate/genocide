# This file is placed in the Public Domain.

import op

tbl = op.Default()

op.update(tbl, {"modnames": {"cfg": "op.cmd.cfg", "cmd": "op.cmd.cmd", "dlt": "op.usr", "flt": "op.cmd.adm", "fnd": "op.cmd.fnd", "krn": "op.cmd.adm", "met": "op.usr", "mod": "op.cmd.adm", "thr": "op.cmd.adm", "upt": "op.cmd.adm", "ver": "op.ver"}, "names": {"bus": ["op.bus.Bus"], "cfg": ["op.irc.Cfg"], "command": ["op.evt.Command"], "console": ["op.csl.Console"], "core": ["op.hdl.Core"], "dcc": ["op.irc.DCC"], "default": ["op.Default"], "event": ["op.evt.Event", "op.irc.Event"], "getter": ["op.prs.Getter"], "handler": ["op.hdl.Handler"], "irc": ["op.irc.IRC"], "object": ["op.Object"], "objectlist": ["op.ObjectList"], "option": ["op.prs.Option"], "repeater": ["op.clk.Repeater"], "select": ["op.sel.Select"], "selectconsole": ["op.csl.SelectConsole"], "setter": ["op.prs.Setter"], "shell": ["op.csl.Shell"], "skip": ["op.prs.Skip"], "test": ["op.csl.Test"], "timed": ["op.prs.Timed"], "timer": ["op.clk.Timer"], "token": ["op.prs.Token"], "user": ["op.usr.User"], "users": ["op.usr.Users"]}, "pnames": {"adm": "op.cmd.adm", "bus": "op.bus", "cfg": "op.cmd.cfg", "clk": "op.clk", "cmd": "op.cmd.cmd", "csl": "op.csl", "dbs": "op.dbs", "evt": "op.evt", "fnd": "op.cmd.fnd", "hdl": "op.hdl", "irc": "op.irc", "itr": "op.itr", "prs": "op.prs", "sel": "op.sel", "tbl": "op.tbl", "thr": "op.thr", "usr": "op.usr", "utl": "op.utl", "ver": "op.ver"}})
