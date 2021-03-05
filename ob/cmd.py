# This file is placed in the Public Domain.

"commands"

# imports

from .hdl import Bus, Handler

# commands

def cmd(event):
    b = Bus.by_orig(event.orig)
    event.reply(",".join(sorted(Handler.cmds)))
