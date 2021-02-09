# This file is placed in the Public Domain.

import os, shutil

from gcd.obj import Object, save, update
from gcd.prs import parse
from gcd.run import cfg

def cp(event):
    if not os.path.exists(cfg.md):
        os.mkdir(cfg.md)
    fns = []
    mpath = os.path.abspath(os.path.join(os.getcwd(), "mod"))
    for fn in os.listdir(mpath):
        if not fn.endswith("py"):
            continue
        fns.append("mod/%s" % fn)
    for fn in fns:
        fnn = os.path.join(cfg.wd, fn)
        shutil.copy2(fn, fnn)
    event.reply("ok")

def set(event):
    p = Object()
    parse(p, event.rest)
    update(cfg, p)
    save(cfg)
    event.reply("ok")

def sys(event):
    event.reply(format(cfg))
