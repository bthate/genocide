# This file is placed in the Public Domain.
# pylint: disable=C,I,R

"""write your own commands


The ``genocide`` package provides an Object class, that mimics a dict while
using attribute access and provides a save/load to/from json files on disk.
Objects can be searched with database functions and uses read-only files
to improve persistence and a type in filename for reconstruction. Methods
are factored out into functions to have a clean namespace to read JSON data
into.

basic usage is this::

 >>> from genocide import Object
 >>> o = Object()
 >>> o.key = "value"
 >>> o.key
 >>> 'value'

Objects try to mimic a dictionary while trying to be an object with normal
attribute access as well. hidden methods are provided, the methods are
factored out into functions like get, items, keys, register, set, update
and values.

read/write from/to disk::

 >>> from genocide import Object, read, write
 >>> o = Object()
 >>> o.key = "value"
 >>> p = write(o)
 >>> obj = Object()
 >>> read(obj, p)
 >>> obj.key
 >>> 'value'

great for giving objects peristence by having their state stored in files::

 >>> from genocide import Object, write
 >>> o = Object()
 >>> write(o)
 genocide.objects.Object/89efa5fd7ad9497b96fdcb5f01477320/2022-11-21/17:20:12.2

"""


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


from genocide import classes, clients, default, loggers, objects, persist, runtime
from genocide import threads


from genocide.classes import Classes
from genocide.clients import Client
from genocide.default import Default
from genocide.loggers import Logging
from genocide.objects import Object, edit, items, keys, kind, prt, search, update
from genocide.objects import values
from genocide.persist import Persist, find, last, read, write
from genocide.runtime import Cfg
from genocide.threads import launch


def __dir__():
    return (
            "Cfg",
            "Classes",
            "Client",
            "Default",
            'Logging',
            "Object",
            "Persist",
            'edit',
            'find',
            'items',
            'keys',
            'kind',
            'last',
            "launch",
            'prt',
            'read',
            'search',
            'update',
            'values',
            'write'
           )


__all__ = __dir__()
