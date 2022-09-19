# This file is placed in the Public Domain.
# pylint: disable=C0114,C0115,C0116


"json"


import datetime
import json
import os


from json import JSONDecoder, JSONEncoder


from cide.obj import Object, update
from cide.utl import cdir
from cide.wdr import Wd


def __dir__():
    return (
            'ObjectDecoder',
            'ObjectEncoder',
            'dump',
            'dumps',
            'load',
            'loads',
            'save'
           )


class ObjectDecoder(JSONDecoder):

    def  __init__(self, *args, **kwargs):
        JSONDecoder.__init__(self, *args, **kwargs)

    def decode(self, s, _w=None):
        value = json.loads(s)
        return Object(value)

    def raw_decode(self, s, *args, **kwargs):
        return JSONDecoder.raw_decode(self, s, *args, **kwargs)


class ObjectEncoder(JSONEncoder):

    "object encoder (object to text)."

    def  __init__(self, *args, **kwargs):
        JSONEncoder.__init__(self, *args, **kwargs)

    def encode(self, o):
        return JSONEncoder.encode(self, o)

    def default(self, o):
        if isinstance(o, dict):
            return o.items()
        if isinstance(o, Object):
            return vars(o)
        if isinstance(o, list):
            return iter(o)
        if isinstance(o,
                      (type(str), type(True), type(False),
                       type(int), type(float))
                     ):
            return o
        try:
            return JSONEncoder.default(self, o)
        except TypeError:
            return str(o)

    def iterencode(self, o, *args, **kwargs):
        return JSONEncoder.iterencode(self, o, *args, **kwargs)


def dump(obj, opath):
    cdir(opath)
    with open(opath, "w", encoding="utf-8") as ofile:
        json.dump(
            obj.__dict__, ofile, cls=ObjectEncoder, indent=4, sort_keys=True
        )
    return obj.__stp__


def dumps(obj):
    return json.dumps(obj, cls=ObjectEncoder)


def hook(path):
    obj = Object()
    load(obj, path)
    return obj


def load(obj, opath):
    splitted = opath.split(os.sep)
    stp = os.sep.join(splitted[-4:])
    lpath = os.path.join(Wd.workdir, "store", stp)
    if os.path.exists(lpath):
        with open(lpath, "r", encoding="utf-8") as ofile:
            res = json.load(ofile, cls=ObjectDecoder)
            update(obj, res)
    obj.__stp__ = stp


def loads(jss):
    return json.loads(jss, cls=ObjectDecoder)


def save(obj):
    prv = os.sep.join(obj.__stp__.split(os.sep)[:1])
    obj.__stp__ = os.path.join(
                       prv,
                       os.sep.join(str(datetime.datetime.now()).split())
                      )
    opath = Wd.getpath(obj.__stp__)
    dump(obj, opath)
    os.chmod(opath, 0o444)
    return obj.__stp__
