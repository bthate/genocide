# OPL - object progamming library (tbl.py)
#
# this file is placed in the public domain

"tables (tbl)"

import opl

#:
names = opl.Ol({
         "bus": ["opl.hdl.Bus"],
         "cfg": ["opl.udp.Cfg", "opl.Cfg", "opl.irc.Cfg", "opl.rss.Cfg"],
         "command": ["opl.hdl.Command"],
         "dcc": ["opl.irc.DCC"],
         "default": ["opl.Default"],
         "event": ["opl.irc.Event", "opl.hdl.Event"],
         "feed": ["opl.rss.Feed"],
         "fetcher": ["opl.rss.Fetcher"],
         "handler": ["opl.hdl.Handler"],
         "irc": ["opl.irc.IRC"],
         "log": ["opl.cmd.Log"],
         "object": ["opl.Object"],
         "ol": ["opl.Ol"],
         "repeater": ["opl.clk.Repeater"],
         "rss": ["opl.rss.Rss"],
         "timer": ["opl.clk.Timer"],
         "todo": ["opl.cmd.Todo"],
         "udp": ["opl.udp.UDP"],
         "user": ["opl.usr.User"],
         "users": ["opl.usr.Users"]
        })
