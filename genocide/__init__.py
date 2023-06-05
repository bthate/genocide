# This file is placed in the Public Domain
#
# pylama: ignore=E402,W0611,W0401,C901


"""object programming runtime


OPR is runtime kit that uses object programming for it's implementation.
Object programming uses classes with the methods factored out into
functions, to get a clean namespace to load json into and not overwrite
any methods. A clean namespace way of programming, so to speak.

OPR provides object persistence, an event handler and some basic code to
load modules that can provide additional commands.

OPR has some functionality, mostly feeding RSS feeds into a irc
channel. It can do some logging of txt and take note of things todo.

OPR is placed in the Public Domain.

"""


from . import clients, clocked, command, configs, decoder, default, defines
from . import encoder, errored, evented, handler, listens, logging, objects
from . import objfunc, parsers, persist, repeats, runtime, threads, utility


from .objects import *
from .objfunc import *
from .command import Commands
from .persist import *


def __dir__():
    return (
            'Object',
            'copy',
            'dump',
            'dumprec',
            'edit',
            'ident',
            'items',
            'keys',
            'kind',
            'load',
            'prt',
            'read',
            'readrec',
            'search',
            'update',
            'values',
            'write',
            'writerec'
           )


__all__ = __dir__()
