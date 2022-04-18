# This file is placed in the Public Domain.


"object callback"


from obj import Object, get
from ofn import register
from oth import launch


def __dir__():
    return (
        "Callback",
    )


class Callback(Object):

    cbs = Object()
    errors = []
    threaded = True

    @staticmethod
    def add(name, cb):
        register(Callback.cbs, name, cb)

    @staticmethod
    def callback(e):
        f = Callback.get(e.type)
        if f:
            try:
                f(e)
            except Exception as ex:
                Callback.errors.append(ex)
                e.exc = ex
                e.ready()

    @staticmethod
    def get(cmd):
        return get(Callback.cbs, cmd)


    @staticmethod
    def dispatch(e):
        if Callback.threaded:
            e.thrs.append(launch(Callback.callback, e, name=e.txt))
            return
        Callback.callback(e)
