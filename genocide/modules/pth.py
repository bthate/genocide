# This file is placed in the Public Domain.


import os


from genocide.configs import Config
from genocide.message import reply
from genocide.package import get
from genocide.utility import importer

def pth(event):
    mod = importer(f"{Config.name}.nucleus")
    if not mod:
        reply(event, "can't find web directory.")
        return
    path = os.path.join(mod.__path__[0], "index.html")
    reply(event, f"file://{path}")
