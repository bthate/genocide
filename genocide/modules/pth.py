# This file is placed in the Public Domain.


import os


from genocide.package import Mods


def pth(event):
    path = os.path.join(Mods.path, "nucleus")
    event.reply(f"file://{path}")
