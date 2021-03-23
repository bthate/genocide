# This file is in the Public Domain.

from .. import edit, format, save
from ..dbs import last
from ..irc import Cfg

def cfg(event):
    c = Cfg()
    last(c)
    if not event.sets:
        return event.reply(format(c, skip=["username", "realname"]))
    edit(c, event.sets)
    save(c)
    event.reply("ok")
