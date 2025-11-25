# This file is placed in the Public Domain.


from genocide.package import Mods


def mod(event):
    event.reply(",".join(Mods.modules()))
