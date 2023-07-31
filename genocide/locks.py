# This file is placed in the Public Domain.
#
# pylint: disable=C,I,R


"locking"


import _thread


def __dir__():
    return (
            'disklock',
           )


__all__ = __dir__()


disklock = _thread.allocate_lock()
