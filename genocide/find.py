# This file is placed in the Public Domain.


"find objects"


import os
import pathlib
import time


from .disk   import read
from .cache  import Cache
from .object import Object, fqn, items, update


p = os.path.join


class Workdir:

    name = __file__.rsplit(os.sep, maxsplit=2)[-2]
    wdr  = ""


def long(name) -> str:
    split = name.split(".")[-1].lower()
    res = name
    for names in types():
        if split == names.split(".")[-1].lower():
            res = names
            break
    return res


def pidname(name) -> str:
    return p(Workdir.wdr, f"{name}.pid")


def skel() -> str:
    path = pathlib.Path(store())
    path.mkdir(parents=True, exist_ok=True)
    return path


def store(pth="") -> str:
    return p(Workdir.wdr, "store", pth)


def strip(pth, nmr=2) -> str:
    return os.sep.join(pth.split(os.sep)[-nmr:])


def types() -> [str]:
    return os.listdir(store())


"find"


def fns(clz) -> [str]:
    dname = ''
    pth = store(clz)
    for rootdir, dirs, _files in os.walk(pth, topdown=False):
        if dirs:
            for dname in sorted(dirs):
                if dname.count('-') == 2:
                    ddd = p(rootdir, dname)
                    for fll in os.listdir(ddd):
                        yield p(ddd, fll)


def fntime(daystr) -> int:
    datestr = ' '.join(daystr.split(os.sep)[-2:])
    if '.' in datestr:
        datestr, rest = datestr.rsplit('.', 1)
    else:
        rest = ''
    timed = time.mktime(time.strptime(datestr, '%Y-%m-%d %H:%M:%S'))
    if rest:
        timed += float('.' + rest)
    return timed


def find(clz, selector=None, deleted=False, matching=False) -> [Object]:
    skel()
    res = []
    clz = long(clz)
    for fnm in fns(clz):
        obj = Cache.get(fnm)
        if not obj:
            obj = Object()
            read(obj, fnm)
            Cache.add(fnm, obj)
        if not deleted and '__deleted__' in dir(obj) and obj.__deleted__:
            continue
        if selector and not search(obj, selector, matching):
            continue
        res.append((fnm, obj))
    return sorted(res, key=lambda x: fntime(x[0]))


"methods"


def last(obj, selector=None) -> Object:
    if selector is None:
        selector = {}
    result = sorted(
                    find(fqn(obj), selector),
                    key=lambda x: fntime(x[0])
                   )
    res = None
    if result:
        inp = result[-1]
        update(obj, inp[-1])
        res = inp[0]
    return res


def search(obj, selector, matching=None) -> bool:
    res = False
    if not selector:
        return res
    for key, value in items(selector):
        val = getattr(obj, key, None)
        if not val:
            continue
        if matching and value == val:
            res = True
        elif str(value).lower() in str(val).lower() or value == "match":
            res = True
        else:
            res = False
            break
    return res


def __dir__():
    return (
        'Workdir',
        'fns',
        'fntime',
        'find',
        'last',
        'pidname',
        'search',
        'skel',
        'types'
    )
