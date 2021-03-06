# This file is placed in the Public Domain.

"object class"

# imports

import datetime
import importlib
import json
import os
import random
import sys
import types
import uuid

# exceptions

class ENOFILENAME(Exception):

    pass

# classes

class O:

    __slots__ = ("__dict__", "__id__", "__type__", "__stp__")

    def __init__(self):
        self.__id__ = str(uuid.uuid4())
        self.__type__ = get_type(self)
        timestamp = str(datetime.datetime.now()).split()
        self.__stp__ = os.path.join(self.__type__, self.__id__, os.sep.join(timestamp))

    def __delitem__(self, k):
        try:
            del self.__dict__[k]
        except KeyError:
            pass

    def __getitem__(self, k):
        return self.__dict__[k]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __lt__(self, o):
        return len(self) < len(o)

    def __setitem__(self, k, v):
        self.__dict__[k] = v

    def __str__(self):
        return json.dumps(self, default=default, sort_keys=True)

class Object(O):

    def __init__(self, *args, **kwargs):
        super().__init__()
        if args:
            try:
                v = vars(args[0])
            except TypeError:
                v = args[0]
            self.__dict__.update(v)

class ObjectList(Object):

    def append(self, key, value):
        if key not in self:
            self[key] = []
        if value in self[key]:
            return
        if isinstance(value, list):
            self[key].extend(value)
        else:
            self[key].append(value)

    def update(self, d):
        for k, v in items(d):
            self.append(k, v)

class Default(Object):

    default = ""

    def __getattr__(self, k):
        try:
            return super().__getattribute__(k)
        except AttributeError:
            try:
                return super().__getitem__(k)
            except KeyError:
                return self.default

class Cfg(Default):

    pass

# functions

def cdir(path):
    if os.path.exists(path):
        return
    res = ""
    path2, _fn = os.path.split(path)
    for p in path2.split(os.sep):
        res += "%s%s" % (p, os.sep)
        padje = os.path.abspath(os.path.normpath(res))
        try:
            os.mkdir(padje)
            os.chmod(padje, 0o700)
        except (IsADirectoryError, NotADirectoryError, FileExistsError):
            pass

def direct(name, pname=''):
    if name in sys.modules:
        return sys.modules[name]
    return importlib.import_module(name, pname)
            
def e(p):
    return os.path.expanduser(p)

def get_cls(fullname):
    try:
        modname, clsname = fullname.rsplit(".", 1)
    except Exception as ex:
        raise ENOCLASS(fullname)
    import sys
    mod = importlib.import_module(modname)
    return getattr(mod, clsname)

def hook(hfn):
    if hfn.count(os.sep) > 3:
        oname = hfn.split(os.sep)[-4:]
    else:
        oname = hfn.split(os.sep)
    cname = oname[0]
    fn = os.sep.join(oname)
    o = get_cls(cname)()
    load(o, fn)
    return o

def mods(mn):
    mod = []
    for name in spl(mn):
        pkg = direct(name)
        path = list(pkg.__path__)[0]
        for m in ["%s.%s" % (name, x.split(os.sep)[-1][:-3]) for x in os.listdir(path)
                  if x.endswith(".py")
                  and not x == "setup.py"]:
            mod.append(direct(m))
    return mod

def op(ops):
    for opt in ops:
        if opt in cfg.opts:
            return True
    return False

def parse():
    import ob.prs
    ob.prs.parse(cfg, " ".join(sys.argv[1:]))
    ob.update(cfg, cfg.sets)
    return cfg

def spl(txt):
    return [x for x in txt.split(",") if x]

# object functions

def default(o):
    if isinstance(o, Object):
        return vars(o)
    if isinstance(o, dict):
        return o.items()
    if isinstance(o, list):
        return iter(o)
    if isinstance(o, (type(str), type(True), type(False), type(int), type(float))):
        return o
    return repr(o)

def edit(o, setter, skip=False):
    try:
        setter = vars(setter)
    except (TypeError, ValueError):
        pass
    if not setter:
        setter = {}
    count = 0
    for key, v in ob.items(setter):
        if skip and v == "":
            continue
        count += 1
        if v in ["True", "true"]:
            o[key] = True
        elif v in ["False", "false"]:
            o[key] = False
        else:
            o[key] = v
    return count

def format(o, keys=None, skip=None, empty=True):
    if keys is None:
        keys = vars(o).keys()
    if skip is None:
        skip = []
    res = []
    txt = ""
    for key in keys:
        if key in skip:
            continue
        try:
            val = o[key]
        except KeyError:
            continue
        if empty and not val:
            continue
        val = str(val).strip()
        res.append((key, val))
    result = []
    for k, v in res:
        result.append("%s=%s%s" % (k, v, " "))
    txt += " ".join([x.strip() for x in result])
    return txt.strip()


def get(o, k, d=None):
    if isinstance(o, dict):
        return o.get(k, d)
    return o.__dict__.get(k, d)

def get_name(o):
    t = type(o)
    if t == types.ModuleType:
        return o.__name__
    try:
        n = "%s.%s" % (o.__self__.__class__.__name__, o.__name__)
    except AttributeError:
        try:
            n = "%s.%s" % (o.__class__.__name__, o.__name__)
        except AttributeError:
            try:
                n = o.__class__.__name__
            except AttributeError:
                n = o.__name__
    return n

def get_type(o):
    t = type(o)
    if t == type:
        try:
            return "%s.%s" % (o.__module__, o.__name__)
        except AttributeError:
            pass
    return str(type(o)).split()[-1][1:-2]

def items(o):
    try:
        return o.items()
    except (TypeError, AttributeError):
        return o.__dict__.items()

def j(*args):
    return os.path.join(*args)

def keys(o):
    return o.__dict__.keys()

def load(o, opath):
    assert opath
    assert cfg.wd
    if opath.count(os.sep) != 3:
        raise ENOFILENAME(opath)
    spl = opath.split(os.sep)
    stp = os.sep.join(spl[-4:])
    lpath = os.path.join(cfg.wd, "store", stp)
    o.__type__ = spl[0]
    o.__id__ = spl[1]
    with open(lpath, "r") as ofile:
        try:
            update(o, json.load(ofile, object_hook=Object))
        except json.decoder.JSONDecodeError as ex:
            return
    return stp

def overlay(o, d, keys=None):
    for k, v in items(d):
        if keys and k not in keys:
            continue
        if v:
            o[k] = v

def register(o, k, v):
    o[k] = v

def save(o):
    timestamp = str(datetime.datetime.now()).split()
    o.__stp__ = os.path.join(o.__type__, o.__id__, os.sep.join(timestamp))
    opath = os.path.join(cfg.wd, "store", o.__stp__)
    cdir(opath)
    with open(opath, "w") as ofile:
        json.dump(o, ofile, default=default)
    os.chmod(opath, 0o444)
    return o.__stp__

def set(o, k, v):
    setattr(o, k, v)

def update(o, d):
    try:
        return o.__dict__.update(vars(d))
    except TypeError:
        return o.__dict__.update(d)

def values(o):
    return o.__dict__.values()

# commands

def krn(event):
    if not event.sets:
        event.reply(format(cfg, skip=["old", "opts", "res", "sets"]))
        return
    edit(cfg, event.sets)
    save(cfg)
    event.reply("ok")

def mod(event):
    event.reply(",".join(sorted({x.split(".")[-1] for x in find_modules(ob.cfg.pkgs)})))

# runtime

cfg = Cfg()
cfg.autoload = False
cfg.debug = False
cfg.name = "ob"
cfg.pkgs = "ob,mod"
cfg.verbose = False
cfg.wd = ""

import ob.bus
import ob.evt
import ob.prs
import ob.thr
import ob.dbs
import ob.hdl
import ob.shl
import ob.trm
import ob.itr
