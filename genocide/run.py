# This file is placed in the Public Domain.
# pylint: disable=R,C,W,C0302


"runtime"


## import


import inspect
import os
import sys
import traceback


from .obj import Default


## define


def __dir__():
    return (
            'Cfg',
           )


__all__ = __dir__()


## runtime


Cfg = Default()


