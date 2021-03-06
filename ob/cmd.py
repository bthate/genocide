# This file is placed in the Public Domain.

"commands"

# imports

import ob

# commands

def cmd(event):
    b = ob.bus.Bus.by_orig(event.orig)
    event.reply(",".join(sorted(b.cmds)))
