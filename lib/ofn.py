# This file is placed in the Public Domain.


"object functions"


import os
import pathlib


from obj import Object, items, keys
from oul import spl


def __dir__():
    return (
        "diff",
        "edit",
        "format",
        "register",
        "search"
    )


def diff(o1, o2):
    d = Object()
    for k in keys(o2):
        if k in keys(o1) and o1[k] != o2[k]:
            d[k] = o2[k]
    return d


def edit(o, setter):
    for key, v in items(setter):
        register(o, key, v)


def format(o, args="", skip="", sep=" ", empty=False, **kwargs):
    res = []
    if args:
        ks = spl(args)
    else:
        ks = keys(o)
    for k in ks:
        if k in spl(skip) or k.startswith("_"):
            continue
        v = getattr(o, k, None)
        if not v and not empty:
            continue
        if isinstance(v, str) and len(v.split()) >= 2:
            txt = '%s="%s"' % (k, v)
        else:
            txt='%s=%s' % (k, v)
        res.append(txt)
    return sep.join(res)


def register(o, k, v):
    setattr(o, k, v)


def search(o, s):
    ok = False
    for k, v in items(s):
        vv = getattr(o, k, None)
        if v not in str(vv):
            ok = False
            break
        ok = True
    return ok
