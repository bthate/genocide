# This file is placed in the Public Domain.


"configurations"


from genocide.objects import Object


class Default(Object):

    def __getattr__(self, key):
        return self.__dict__.get(key, "")


class Config(Default):

    name = "genocide"
    opts = ""
    sets = Default()
    version = 220


def __dir__():
    return (
        'Config',
    )
    